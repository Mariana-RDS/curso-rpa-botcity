"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot
from botcity.plugins.csv import BotCSVPlugin

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Instancie o plugin
    planilha = BotCSVPlugin()

    dados = planilha.read(r"resources\items.csv").as_list()


    bot = DesktopBot()
    bot.browse("C:\Program Files\Fakturama2\Fakturama.exe")

    # Implement here your logic...
    bot.execute(r"C:\Program Files\Fakturama2\Fakturama.exe")

    for item in dados:

        # Searching for element 'new_product'
        if not bot.find("new_product", matching=0.97, waiting_time=50000):
            not_found("new_product")
        bot.click()

        # Searching for element 'item_number'
        if not bot.find("item_number", matching=0.97, waiting_time=60000):
            not_found("item_number")
        bot.click_relative(192, 10)

        # item number
        bot.paste(item[1])
        bot.tab()

        # name
        bot.paste(item[2])
        bot.tab()

        # category
        bot.paste(item[3])
        bot.tab()

        # GTIN
        bot.paste(item[4])
        bot.tab()

        # supcode
        bot.paste(item[5])
        bot.tab()

        # description
        bot.paste(item[6])
        bot.tab()

        # price
        bot.control_a()
        bot.paste(item[7])
        bot.tab()

        # costprice
        bot.control_a()
        bot.paste(item[8])
        bot.tab()

        # allowace
        bot.control_a()
        bot.paste(item[9])
        bot.tab()

        # VATNAME
        # Searching for element 'VAT'
        if not bot.find("VAT", matching=0.97, waiting_time=10000):
            not_found("VAT")
        bot.click_relative(128, 13)
        # Searching for element 'vat_n'
        if not bot.find("vat_n", matching=0.97, waiting_time=10000):
            not_found("vat_n")
        bot.click()
        bot.tab()

        #quantity
        bot.control_a()
        bot.paste(item[14])

        # image
        # Searching for element 'image'
        # if not bot.find("image", matching=0.97, waiting_time=70000):
        #     not_found("image")
        # bot.click()

        # bot.paste(rf"C:\Users\mard_\OneDrive\Área de Trabalho\produtos\bot-fakturama\resources\imagens_produtos\{item[13]}")
        # bot.enter()

        # save
        # Searching for element 'save'
        if not bot.find("save", matching=0.97, waiting_time=10000):
            not_found("save")
        bot.click()

        # Fechar form
        bot.control_w()

    # fechar fakturama
    bot.alt_f4()










    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK.",
    #     total_items=0,
    #     processed_items=0,
    #     failed_items=0
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()