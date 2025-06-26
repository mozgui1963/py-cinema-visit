from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[Customer], hall_number: int, cleaner: str, movie: str) -> None:
    customer_obj = [Customer(customer["name"], customer["food"])
                    for customer in customers]
    for customer in customer_obj:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(hall_number)
    clr = Cleaner(cleaner)
    CinemaHall.movie_session(hall,
                             movie_name=movie,
                             customers=customer_obj, 
                             cleaning_staff=clr)
