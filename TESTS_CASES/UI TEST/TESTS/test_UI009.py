import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Para ver el fallo si es necesario
        yield browser
        browser.close()

def test_image_incorrect_inventory(browser):
    page = browser.new_page()

    # 1. Ir a la página de login
    page.goto('https://www.saucedemo.com/')

    # 2. Ingresar credenciales válidas
    page.fill('input[name="user-name"]', 'visual_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')

    # 3. Esperar a que la página de inventario cargue
    page.wait_for_selector(".inventory_list", timeout=5000)

    # 4. Obtener el atributo src de la imagen incorrecta
    img_inventory_src = page.query_selector('#item_4_img_link > img').get_attribute('src')

    # 5. Hacer clic en el producto Sauce Labs backpack para ir a la página de detalles
    page.click('#item_4_img_link')

    # 6. Esperar que la página del producto se cargue
    page.wait_for_selector('#inventory_item_container', timeout=5000)

    # 7. Obtener el atributo src de la imagen correcta
    img_product_src = page.query_selector('#inventory_item_container > div > div > div.inventory_details_img_container > img').get_attribute('src')

    # 8. Validar que las imágenes no sean iguales
    assert img_inventory_src != img_product_src, "La imagen en el inventario es incorrecta"
    
    page.close()
