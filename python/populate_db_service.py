from faker import Faker
import json
import mysql.connector
from random import randint

fake = Faker()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="db-pass",
    database="testDB"
)
myCursor = mydb.cursor(dictionary=True)

# fake.uuid4(),
# fake.random_int(min=100000, max=999999),
# fake.date_this_decade(),
# fake.word(),
# fake.random_int(min=500, max=2000),
# fake.date_between(start_date='today', end_date='+10y'),
# fake.currency_code(),
# fake.boolean(),
# fake.pydecimal(left_digits=3, right_digits=2, positive=True)
# fake.pystr(min_chars=None, max_chars=l)

def decimal():
    return fake.pydecimal(left_digits=3, right_digits=2, positive=True)


def fake_int():
    return fake.pydecimal(left_digits=3, right_digits=0, positive=True)


def fetch_ids():
    global pax_ids, payment_ids, user_ids, booking_ids
    myCursor.execute('select id_ from booking_pax_details limit 10')
    pax_ids = list(next(iter(v)) for v in myCursor.fetchall())
    myCursor.execute('select id_ from booking_payment_details limit 10')
    payment_ids = list(next(iter(v)) for v in myCursor.fetchall())
    myCursor.execute('select userId from user_ limit 10')
    user_ids = list(next(iter(v)) for v in myCursor.fetchall())
    myCursor.execute('select id_ from booking_details order by id_ desc limit 10')
    booking_ids = list(next(iter(v)) for v in myCursor.fetchall())


def random_item_from(items):
    return fake.random_element(elements=items)


def generate_di_ticket_row():
    global values
    fake_data = {
        "booking_pax_details_id": random_item_from(pax_ids),
        "booking_payment_details_id": random_item_from(payment_ids),
        "invoice_number": fake_string_with_len(10),
        "invoice_date": fake.date_between(start_date='-2y', end_date='today'),
        "booked_date": fake.date_between(start_date='-2y', end_date='today'),
        "ticket_status": fake.random_element(elements=('booked', 'cancelled', 'refunded')),
        "validating_carrier": fake_string_with_len(10),
        "full_fare": decimal(),
        "reason_code": fake.word(),
        "total_fare": decimal(),
        "base_fare": decimal(),
        "taxes": decimal(),
        "booking_fee": decimal(),
        "markup": decimal(),
        "refunded_amount": decimal(),
        "modification_charge": decimal(),
        "pnr": fake.word(),
        "flight_type": random_item_from(('domestic', 'international')),
        "transaction_type": random_item_from(('VOID', 'REFUND')),
        "departure_date": fake.date_between(start_date='-2y', end_date='today'),
        "arrival_date": fake.date_between(start_date='-2y', end_date='today'),
        "currency_code": fake.pystr(min_chars=None, max_chars=3),
        "is_exchange_ticket": int(fake.boolean()),
        "booking_origination_type": random_item_from(('AUTO', 'MANUAL')),
        "ticket_mode": random_item_from(('AIR', 'RAIL')),
        "route": fake.word(),
        "original_ticket_number": fake.word(),
        "original_validating_carrier": fake_string_with_len(10),
        "commission": fake.pydecimal(),
        "tour_code": fake.word(),
        "tax1": decimal(),
        "tax2": decimal(),
        "tax3": decimal(),
        "tax4": decimal(),
        # "ticket_endorsement_remarks": ,
        # "fare_calculation": ,
        # "policy_override": ,
        # "negotiated_rate": ,
        # "alternate_carrier": ,
        # "alternate_carrier_flight_number": ,
        # "osi_remarks": ,
        # "free_ticket": ,
        # "pos_country_code": ,
        "created_by": random_item_from(user_ids),
        # "creation_date": ,
        "modified_by": random_item_from(user_ids),
        # "modification_date":
    }
    # print(fake_data)
    fields = ', '.join(fake_data.keys())
    values = ', '.join(['"{0}"'.format(value) for value in fake_data.values()])
    # print(fields)
    # print(values)
    sql = f'INSERT INTO di_tickets ({fields}) VALUES ({values})'
    myCursor.execute(sql)
    mydb.commit()


def generate_di_segment_row():
    global segment_values
    fake_data = {
        "segment_id": fake_int(),
        "booking_details_id": random_item_from(booking_ids),
        "marketing_airline_code": fake_string_with_len(2),
        "operating_airline_code": fake_string_with_len(2),
        "origin_code": fake_string_with_len(6),
        "destination_code": fake_string_with_len(6),
        "departure_date": fake.date_between(start_date='-2y', end_date='today'),
        # "departure_time":
        "departure_terminal": fake.word(),
        "arrival_date": fake.date_between(start_date='-2y', end_date='today'),
        # "arrival_time":
        "arrival_terminal": fake.word(),
        "duration": fake_int(),
        "layover_duration": fake_int(),
        "brand": fake.word(),
        "class_of_service": fake_string_with_len(2),
        "fare_basis_code": fake_string_with_len(15),
        "marketing_flight_number": fake_string_with_len(4),
        "operating_flight_number": fake_string_with_len(4),
        "leg_number": fake_int(),
        "sequence_number": fake_int(),
        "connection_type": random_item_from(('CONNECTION', 'DESTINATION')),
        "segment_mode": random_item_from(('AIR', 'RAIL')),
        "segment_type": random_item_from(('domestic', 'international', 'transborder')),
        "ticket_designator":fake_string_with_len(10),
        "actual_segment_fare":decimal(),
        "miscellaneous_charges":decimal(),
        # "segment_miles":
        "created_by":random_item_from(user_ids),
        "creation_date":fake.date_between(start_date='-2y', end_date='today'),
        "modified_by":random_item_from(user_ids),
        "modification_date":fake.date_between(start_date='-2y', end_date='today')
    }
    # print(fake_data)
    fields = ', '.join(fake_data.keys())
    segment_values = ', '.join(['"{0}"'.format(value) for value in fake_data.values()])
    # print(fields)
    # print(values)
    sql = f'INSERT INTO di_segments ({fields}) VALUES ({segment_values})'
    myCursor.execute(sql)
    mydb.commit()


def print_ids():
    print('pax', pax_ids)
    print('cards', payment_ids)
    print('users', user_ids)
    print('bookings', booking_ids)


def fake_string_with_len(l):
    return fake.pystr(min_chars=None, max_chars=l)

def connect_tickets_with_segments():
    myCursor.execute(' select * from di_tickets ')
    tickets = myCursor.fetchall()
    myCursor.execute(' select * from di_segments ')
    segments = myCursor.fetchall()
    print(tickets[0])
    print(segments[0])
    values = []
    for i in range(5):
      values.append((tickets[i]['ticket_id'],random_item_from(id['segment_id'] for id in segments)))
      values.append((tickets[i]['ticket_id'],random_item_from(id['segment_id'] for id in segments)))
    # print('values', values)
    # myCursor.executemany(" insert into di_ticket_segments values (%s, %s)", values)
    # mydb.commit()
fetch_ids()
print_ids()
connect_tickets_with_segments()
# for i in range(10):
    # generate_di_ticket_row()
    # generate_di_segment_row()
# myCursor.execute(' select * from di_tickets ')
# tickets = myCursor.fetchall()
# for t in tickets:
#     print(t)
