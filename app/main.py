from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer = Customer()
    cine = CinemaHall()
    cleaner = Cleaner()

    CinemaBar.sell_product(customer, CinemaBar.product)
    CinemaHall.movie_session(CinemaHall.movie_name, customer, cleaner)


