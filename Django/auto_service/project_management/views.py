from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Car, CarModel, Order, OrderLine, Service
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    # Let's count some of the main objects
    num_cars = Car.objects.all().count()
    num_models = CarModel.objects.all().count()

    # Order lines which are priced below 100
    order_lines_below_100 = OrderLine.objects.filter(price__lt=100).count()

    # How many services
    num_services = Service.objects.all().count()

    # We transfer information to ta template through a dictionary "context"
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_cars": num_cars,
        "num_models": num_models,
        "order_lines_below_100": order_lines_below_100,
        "num_services": num_services,
        "num_visits": num_visits,
    }

    # Render index.html with our data in a variable named "context"
    return render(request, "index.html", context=context)


def cars(request):
    paginator = Paginator(Car.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars': paged_cars
    }
    print(cars)
    return render(request, 'cars.html', context=context)


def car(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car.html', {'car': single_car})


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 2
    template_name = 'order_list.html'


def order(request, pk):
    single_order = get_object_or_404(Order, pk=pk)
    return render(request, 'order.html', {'order': single_order})


def search(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(Q(client__icontains=query)
                                        | Q(car_model__make__icontains=query)
                                        | Q(car_model__model__icontains=query)
                                        | Q(plate_number__icontains=query)
                                        | Q(vin_code__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})


class MyOrdersByUserListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'user_orders.html'
    context_object_name = "user_orders"
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('date_due')


class OrderDetails(LoginRequiredMixin, generic.DetailView):
    pass

