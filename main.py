import pygame
import qrcode
from PIL import Image
import os
from pgpyui import textarea, button


# --- Interfaces ---
class IQRCodeGenerator:
    def generate(self, text: str) -> Image.Image | None:
        raise NotImplementedError


class IQRCodeSaver:
    def save(self, img: Image.Image, filename: str) -> None:
        raise NotImplementedError


# --- Implementations ---
class QRCodeGenerator(IQRCodeGenerator):
    def generate(self, text: str) -> Image.Image | None:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        try:
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
            return img
        except qrcode.exceptions.DataOverflowError:
            print("Error: Data too large for QR code.")
            return None
        except Exception as e:
            print(f"Error generating QR code: {e}")
            return None


class QRCodeSaver(IQRCodeSaver):
    def save(self, img: Image.Image, filename: str) -> None:
        try:
            os.makedirs("qr-codes", exist_ok=True)
            filepath = os.path.join("qr-codes", filename)
            img.save(filepath)
            print(f"QR code saved as {filepath}")
        except Exception as e:
            print(f"Error saving QR code: {e}")


# --- Application ---
class QRCodeApp:
    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("QR Code Generator")
        self.background_color = (255, 255, 255)
        self.qr_generator = QRCodeGenerator()
        self.qr_saver = QRCodeSaver()
        self.img = None
        self.img_surface = None
        self.init_ui()

    def init_ui(self):
        self.text_area = textarea.TextArea((50, 50), (1180, 40), 20, 120)
        self.generate_button = button.Button(
            (50, 170), (320, 80), "Generate QR", self.generate_qr, []
        )
        self.save_button = button.Button(
            (50, 265), (320, 60), "Save QR", self.save_qr, []
        )
        self.clear_button = button.Button(
            (50, 340), (320, 60), "Clear QR", self.clear_qr, []
        )

    def generate_qr(self):
        text_data = self.text_area.data_return()
        text = "".join(text_data)
        if text:
            self.img = self.qr_generator.generate(text)
            if self.img:
                self.img_surface = pygame.image.frombuffer(
                    self.img.tobytes(), self.img.size, self.img.mode
                )
                self.img_surface = pygame.transform.scale(
                    self.img_surface,
                    (
                        min(self.width // 2 - 100, self.img.size[0]),
                        min(self.height - 100, self.img.size[1]),
                    ),
                )

    def save_qr(self):
        text_data = self.text_area.data_return()
        text = "".join(text_data)
        if self.img is not None and text:
            filename = (
                text.replace("/", "_").replace("\\", "_").replace(":", "_") + ".png"
            )
            filename = filename[:50]
            self.qr_saver.save(self.img, filename)

    def clear_qr(self):
        self.img = None
        self.img_surface = None

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.text_area.check_events(event)
                self.generate_button.check_events(event)
                self.save_button.check_events(event)
                self.clear_button.check_events(event)

            self.screen.fill(self.background_color)
            self.text_area.draw(self.screen)
            self.generate_button.draw(self.screen)
            self.save_button.draw(self.screen)
            self.clear_button.draw(self.screen)

            if self.img is not None:
                qr_x = self.width // 2 + 50
                qr_y = 95
                self.screen.blit(self.img_surface, (qr_x, qr_y))

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    app = QRCodeApp(1280, 720)
    app.run()
