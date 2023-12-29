from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators(BasePage):
    
    LOCATOR_PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

    LOCATOR_BTN_PHONE = (By.ID, "t-btn-tab-phone")

    LOCATOR_BTN_MAIL = (By.ID, "t-btn-tab-mail")

    LOCATOR_BTN_LOGIN = (By.ID, "t-btn-tab-login")

    LOCATOR_BTN_LS = (By.ID, "t-btn-tab-ls")

    LOCATOR_INPUT_MAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')

    LOCATOR_INPUT_USERNAME = (By.ID, 'username')

    LOCATOR_INPUT_PASSWORD = (By.ID, 'password')

    LOCATOR_BTN_ENTER = (By.ID, 'kc-login')

    LOCATOR_BTN_LOGOUT = (By.ID, 'logout-btn')

    LOCATOR_ERROR_MSG = (By.XPATH, "//span[@id='form-error-message']")

    LOCATOR_EMPTY_USERNAME_MSG = (By.CSS_SELECTOR, '.rt-input-container__meta--error')

    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')

    LOCATOR_REGISTER = (By.XPATH, "//a[@id='kc-register']")

    LOCATOR_ACTIVE_TAB = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')

    LOCATOR_SOCIAL_NETWORK_VK = (By.ID, "oidc_vk")

    LOCATOR_IDENTIFIER_VK = (By.XPATH, "// div[contains(text(), 'Вход в VK ID')]")

    LOCATOR_SOCIAL_NETWORK_OK = (By.ID, "oidc_ok")

    LOCATOR_IDENTIFIER_OK = (By.XPATH, "//div[contains(text(),'Одноклассники')]")

    LOCATOR_SOCIAL_MAIL = (By.ID, "oidc_mail")

    LOCATOR_IDENTIFIER_MAIL = (By.XPATH, "// span[contains(text(), 'Мой Мир@Mail.Ru')]")

    LOCATOR_SOCIAL_YANDEX = (By.ID, "oidc_ya")

    LOCATOR_IDENTIFIER_YANDEX = (By.XPATH, "//*[@id='UserEntryFlow']/form/div/div[1]/h1")

    LOCATOR_AGREEMENT = (By.XPATH, "//a[@class='rt-link rt-link--orange' and @href='https://b2c.passport.rt.ru/sso-static/agreement/agreement.html']")

    LOCATOR_AGREEMENT_ROOT = (By.ID, "root")
