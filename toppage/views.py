from django.shortcuts import render
from django.views.generic import View
from .forms import DataForm, ConvertForm
from .models import Data
import pandas as pd

class index(View):

    def __init__(self):
        self.data = {"forms": DataForm,
                     "data": Data.objects.all()}

    def post(self, request):

        form = DataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()



        return render(request, "toppage/index.html", self.data)


    def get(self, request):



        return render(request, "toppage/index.html", self.data)


class ConvertView(View):
    def __init__(self):
        self.data = {"forms": ConvertForm,}

    def post(self, request):

        d = Data.objects.all().values()

        d = pd.DataFrame(d)

        d['date'] = d['date'].apply(lambda x: x.strftime("%Y/%m/%d %H:%M"))




        form = ConvertForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            dir = f'media/{post.name}.csv'

            d.to_csv(dir, index=False)

            data = self.data
            data['file'] = dir

            return render(request, "toppage/convert.html", data)
            #post.save()

        return render(request, "toppage/convert.html", self.data)


    def get(self, request):

        return render(request, "toppage/convert.html", self.data)