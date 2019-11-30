¬еб-краулер

јвтор: —агалов Ћеонид

ќписание:
ƒанное приложение пердставл€ет собой упрощенную версию сетевого паука

—остав:
main_console - азбор аргументов командной строки и метод main()
work_with_url - содержит соответсвующий класс с методами обработки url
work_with_links - содержит соответсвующий класс с методами, выполн€ющими поиск и обработку найденных ссылок
work_with_threads - содержит класс дл€ обращени€ с потоками
work_with_graph - содержит класс с методами дл€ работы с ссылочным графом,его отрисовкой
test_crawler - тесты дл€ вышеприведенных классов

 онсольна€ верси€ 

ѕримеры запуска консольной версии:

- python main_console --startcrawler {link for start} {depth for search} {count of download threads} {filters}
- python main_console --startcrawler https://lenta.ru 0 1 only_http

- python main_console --startcrawler {link for start} (по умолчанию количество потоков равно 1, а глубина поиска равна 0, фильтер по https ссылкам)
- python main_console --startcrawler https://lenta.ru


¬ конце работы краулера в папке с проектом по€витс€ файл graph.html, открыв который можно увидеть ссылочный граф проделанной краулером работы.
“ак же по€витс€ файл logs.log, в котором будут логи процесса работы с ссылками и их загрузки.

Ѕиблиотеки: 
	BeautifulSoup, requests, re, argparse, bokeh, networkx, logging,
ƒл€ тестов:
	unittests

