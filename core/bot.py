import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from core.driver import init_driver
from brain.ai import SmartBrain
import config
import os

class ZeekBot:
    def __init__(self):
        self.driver = None
        self.brain = SmartBrain()
        self.is_running = False

    def start(self):
        print("Starting ZeekBot Driver...")
        self.driver = init_driver()
        self.driver.get("https://web.whatsapp.com")
        self.is_running = True
        
    def get_qr_screenshot(self):
        """Takes a screenshot of the QR code for the Dashboard"""
        if self.driver:
            # Try to find QR canvas or just screenshot page
            time.sleep(5) 
            self.driver.save_screenshot(config.QR_CODE_PATH)
            return True
        return False

    def send_dm(self, phone_number, message):
        """Sends a message to a specific number"""
        try:
            # WhatsApp URL scheme to open chat directly
            self.driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
            time.sleep(15) # Wait for load
            
            # Press Enter (Logic varies by WA version, usually pressing Enter works if text is pre-filled)
            action = webdriver.ActionChains(self.driver)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Error sending DM: {e}")
            return False

    def check_incoming(self):
        """Scans for unread messages and replies"""
        # (Simplified for brevity - requires finding .unread classes in DOM)
        # This is where you'd hook the AI response
        pass

    def bomb_contacts(self, contact_list):
        """Iterates through list and messages them"""
        for contact in contact_list:
            # AI generates opener
            opener = self.brain.generate_reply("", context=f"Starting new chat with {contact}")
            self.send_dm(contact, opener)
            
            # Sleep to avoid Ban
            sleep_time = random.randint(60, 180) 
            print(f"Sleeping {sleep_time}s before next contact...")
            time.sleep(sleep_time)
