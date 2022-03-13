"""Григорианский календарь в порядковый
Порядковая дата содержит номер года и порядковый номер дня в этом году – оба в целочисленном
 формате. При этом год может быть любым согласно григорианскому календарю, а номер дня – числом
 в интервале от 1 до 366 (чтобы учесть високосные годы). Порядковые даты удобно использовать при
 расчете разницы в днях, когда счет ведется именно в днях, а не месяцах. Например, это может
 касаться 90-дневного периода возврата товара для покупателей, расчета срока годности товаров или
 прогнозируемой даты появления малыша на свет.
Напишите функцию с именем ordinal_date, принимающую на вход три целых числа: день, месяц и год.
Функция должна возвращать порядковый номер заданного дня в указанном году. В основной программе у
пользователя должны запрашиваться день, месяц и год соответственно и выводиться на экран порядковый
 номер дня в заданном году. Программа должна запускаться только в том случае, если она не
 импортирована в виде модуля в другой файл.
"""