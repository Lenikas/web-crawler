���-�������

�����: ������� ������

��������:
������ ���������� ������������ ����� ���������� ������ �������� �����

������:
main_console - ����� ���������� ��������� ������ � ����� main()
work_with_url - �������� �������������� ����� � �������� ��������� url
work_with_links - �������� �������������� ����� � ��������, ������������ ����� � ��������� ��������� ������
work_with_threads - �������� ����� ��� ��������� � ��������
work_with_graph - �������� ����� � �������� ��� ������ � ��������� ������,��� ����������
test_crawler - ����� ��� ��������������� �������

���������� ������ 

������� ������� ���������� ������:

- python main_console --startcrawler {link for start} {depth for search} {count of download threads} {filters}
- python main_console --startcrawler https://lenta.ru 0 1 only_http

- python main_console --startcrawler {link for start} (�� ��������� ���������� ������� ����� 1, � ������� ������ ����� 0, ������� �� https �������)
- python main_console --startcrawler https://lenta.ru


� ����� ������ �������� � ����� � �������� �������� ���� graph.html, ������ ������� ����� ������� ��������� ���� ����������� ��������� ������.
��� �� �������� ���� logs.log, � ������� ����� ���� �������� ������ � �������� � �� ��������.

����������: 
	BeautifulSoup, requests, re, argparse, bokeh, networkx, logging,
��� ������:
	unittests

