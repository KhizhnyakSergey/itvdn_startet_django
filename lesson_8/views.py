import csv
import datetime

from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from lesson_8.models import GameModel, GamerModel, GamerLibraryModel


def upload_data(request):
    with open('vgsales.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                pass
    return HttpResponse("Done!")


# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(name__contains='Hitman')

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(name__exact='Hitman (2016)')

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(name__in=['Hitman (2016)', 'Tetris'])

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(na_sales__gte=11.27)

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(na_sales__lte=0.5)

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(name__startswith='Mo')

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(name__endswith='a')

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(eu_sales__range=range(1, 3))

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(year__day=1)

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(year__year=2000)

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(name__isnull=True)

# class FilterView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.filter(name__regex=r'^(An?/The) +')

class FilterView(ListView):
    template_name = 'gamemodel_list.html'

    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="A") & Q(name__endswith="a") & Q(
    #         name__contains="ma"))

    # queryset = GameModel.objects.filter(Q(name__endswith="a"),
    #                                     name__startswith="A")

    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="Ab") | Q(name__startswith="Ad") | Q(
    #         name__startswith="Mat"))

    queryset = GameModel.objects.filter(
        ~Q(name__startswith="Ab") | ~Q(name__startswith="Ad") | ~Q(
            name__startswith="Mat"))


def relation_filter_view(request):
    data = GamerLibraryModel.objects.filter(gamer__email__contains="a")
    print(data[0].gamer.email)
    # return HttpResponse(data)
    return HttpResponse(data.order_by())


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman")


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    # TODO add reverse
    queryset = GameModel.objects.exclude(name__contains="Hitman").order_by(
        'year')


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").union(
        GameModel.objects.filter(name="Tetris"))


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'

    queryset = GameModel.objects.filter(name="Hitman (2016)").values("name",
                                                                     "platform",
                                                                     "year")

    def get(self, request, *args, **kwargs):
        print(GameModel.objects.filter(name="Hitman (2016)").values("name",
                                                                    "platform",
                                                                    "year"))
        print(list(
            GameModel.objects.all().values_list("name", 'year')))
        return super().get(request, *args, **kwargs)


def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='year')
    print(data)
    return HttpResponse(data)


def get_view(request):
    # TODO try error
    data = GameModel.objects.get(pk=5065)
    print(data)
    return HttpResponse(data)


def create_view(request):
    # myself = GamerModel()
    # myself.email = "admin@admin.com"
    # myself.nickname = "SomeRandomNicknameSave"
    # myself.save()

    # myself = GamerModel(email="admin@admin.com",
    #                     nickname="SomeRandomNicknameSave")
    # myself.save()
    #
    # myself = GamerModel(**{"email": "admin@admin.com",
    #                        "nickname": "SomeRandomNicknameSave"})
    # myself.save()

    # myself = GamerModel.objects.create(**{"email": "admin@admin.com",
    #                                       "nickname": "SomeRandomNicknameCreate"})

    # myself = GamerModel.objects.create(email="admin@admin.com",
    #                                    nickname="SomeRandomNicknameCreate")

    # myself = GamerModel.objects.bulk_create([
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate1"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate2"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate3"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate4")
    # ])

    # my_library = GamerLibraryModel(gamer=GamerModel.objects.get(pk=1),
    #                                size=10)
    # my_library.save()
    # my_library.game.set([GameModel.objects.get(pk=22222),
    #                      GameModel.objects.get(pk=22223)])

    # my_library = GamerLibraryModel.objects.create(
    #     gamer=GamerModel.objects.get(pk=9),
    #     size=10)
    # my_library.game.set([GameModel.objects.get(pk=25000),
    #                      GameModel.objects.get(pk=26000)])

    # my_library = GamerLibraryModel.objects.bulk_create(
    #     [GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10),
    #      GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10)
    #      ])
    # my_friend = GamerModel.objects.get(pk=10)
    # my_friend.update(nickname="MySecondNickname")

    # my_friend = GamerModel.objects.get(pk=6)
    # my_friend.nickname = 'MyFriend'
    # my_friend.save()

    my_friend = GamerModel.objects.filter(pk=7)
    my_friend.update(nickname='MySecondNickname')

    return HttpResponse(my_friend)
