from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='BRL')
        bot.select_place_to_go(input('Para qual lugar você deseja viajar? '))
        bot.select_dates(check_in_date=input('Qual será a data de Check-in? '),
                        check_out_date=input('Qual será a data de Check-out? '))
        bot.select_adults(int(input("Quantos adultos irão? ")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()
        bot.report_results()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise