import datetime


def timedelta(from_now):
	if from_now == 'yes':
		delta = datetime.datetime.now() - datetime.datetime(1970, 1, 1, 0, 0, 0)
	else:
		date = [int(number) for number in input('До какой даты: ').split('-')]
		delta = datetime.datetime(*date) - datetime.datetime(1970, 1, 1, 0, 0, 0)
	return delta.days * 24 * 3600


print(timedelta(input('До сегодняшней даты: ')))
