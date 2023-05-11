-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Description of the case:
SELECT description, year FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND street = 'Chamberlin Street';

-- Activity at courthouse 28/07 at 10:15
SELECT activity, license_plate FROM courthouse_security_logs
WHERE day = 28 AND month = 7 AND year = 2020 AND hour = 10 AND minute = 15;
-- nothing.

-- Activity at courthouse 28/07 to visualize the data
SELECT activity, license_plate FROM courthouse_security_logs
WHERE day = 28 AND month = 7 AND year = 2020 AND hour = 10 AND minute = 15;
-- activity: entrance and exit.

-- Get interviews at 28/07 which contain mention to courthouse
SELECT name, transcript FROM interviews
WHERE year = 2020 AND month = 7 AND day = 28 AND transcript LIKE '%courthouse%';

-- Thief withdrawing some money at ATM(atm) on Fifer Street before Eugene (people) arrives (don't have it) at courthouse(courthouse_security_logs) and
-- left between 10:15 and 15:25 and License_plates which have calls, less than a minute between 10:15 and 10:25 on that day
SELECT COUNT(bank_accounts.account_number) FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2020 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Fifer Street'
AND atm_transactions.transaction_type = 'withdraw' AND license_plate IN (SELECT license_plate FROM courthouse_security_logs
WHERE id IN (SELECT id FROM courthouse_security_logs
WHERE activity = 'exit' AND hour = 10 AND minute <= 25 AND day = 28 AND month = 7 AND year = 2020));
-- 4 bank accounts / 4 possible people

-- License plate which exit between 10:15 and 10:25
SELECT COUNT(license_plate) FROM courthouse_security_logs
WHERE id IN (SELECT id FROM courthouse_security_logs
WHERE activity = 'exit' AND hour = 10 AND minute <= 25 AND day = 28 AND month = 7 AND year = 2020);
-- 8 vehicles

--  arrives after Eugene to courthouse
SELECT day, month, hour, minute FROM courthouse_security_logs
WHERE license_plate IN (SELECT license_plate FROM people WHERE name = 'Eugene');
-- Eugene not in courthouse by car at that day. He was walking!

-- License_plates which have calls, less than a minute between 10:15 and 10:25 on that day
SELECT license_plate from people WHERE phone_number IN (
SELECT caller FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60);

-- Thief withdrawing some money at ATM(atm) on Fifer Street before Eugene (people) arrives (don't have it) at courthouse(courthouse_security_logs) and
-- left between 10:15 and 15:25 and License_plates which have calls, less than a minute between 10:15 and 10:25 on that day
SELECT bank_accounts.account_number FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2020 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Fifer Street'
AND atm_transactions.transaction_type = 'withdraw' AND license_plate IN (SELECT license_plate FROM courthouse_security_logs
WHERE license_plate IN (SELECT license_plate from people WHERE phone_number IN (
SELECT caller FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60)) AND id IN (SELECT id FROM courthouse_security_logs
WHERE activity = 'exit' AND hour = 10 AND minute <= 25 AND day = 28 AND month = 7 AND year = 2020));
-- 2 bank accounts / 2 possible people

-- airport id = Fiftyville
SELECT id FROM airports WHERE city = 'Fiftyville';

-- flights id where origin_id = id Fiftyville 29/07/2020 and min hour
SELECT id, hour, minute FROM flights WHERE day = 29 AND month = 7 AND year = 2020 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
AND hour = (SELECT MIN(hour) FROM flights WHERE day = 29 AND month = 7 AND year = 2020);
-- only one flight at 8 am, the earliest.

-- Earlist flight on 29/07/2020
SELECT MIN(hour) FROM flights WHERE day = 29 AND month = 7 AND year = 2020;

-- passports from that flight
SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE day = 29 AND month = 7 AND year = 2020 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
AND hour = (SELECT MIN(hour) FROM flights WHERE day = 29 AND month = 7 AND year = 2020));

-- Thief name: relates passports to people and bank account to people's id (EVERYTHING TOGETHER). THE THIEF IS:
SELECT name FROM people
WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE day = 29 AND month = 7 AND year = 2020 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
AND hour = (SELECT MIN(hour) FROM flights WHERE day = 29 AND month = 7 AND year = 2020)))
AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT bank_accounts.account_number FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2020 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Fifer Street'
AND atm_transactions.transaction_type = 'withdraw' AND license_plate IN (SELECT license_plate FROM courthouse_security_logs
WHERE license_plate IN (SELECT license_plate from people WHERE phone_number IN (
SELECT caller FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60)) AND id IN (SELECT id FROM courthouse_security_logs
WHERE activity = 'exit' AND hour = 10 AND minute <= 25 AND day = 28 AND month = 7 AND year = 2020))));

-- Thief destination: city where the thief's flight heads to (destination) where his passport were at origin airport at that day
SELECT city FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
JOIN passengers ON flights.id = passengers.flight_id
WHERE passport_number IN (SELECT passport_number FROM people
WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights
WHERE day = 29 AND month = 7 AND year = 2020 AND origin_airport_id = (SELECT id FROM airports
WHERE city = 'Fiftyville')
AND hour = (SELECT MIN(hour) FROM flights WHERE day = 29 AND month = 7 AND year = 2020)))
AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT bank_accounts.account_number FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2020 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Fifer Street'
AND atm_transactions.transaction_type = 'withdraw' AND license_plate IN (SELECT license_plate FROM courthouse_security_logs
WHERE license_plate IN (SELECT license_plate from people WHERE phone_number IN (
SELECT caller FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60)) AND id IN (SELECT id FROM courthouse_security_logs
WHERE activity = 'exit' AND hour = 10 AND minute <= 25 AND day = 28 AND month = 7 AND year = 2020)))));

-- Thief destination: in a better way as I know the thiefs name
SELECT city FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
WHERE day = 29 AND month = 7 AND year = 2020 AND origin_airport_id = (SELECT id FROM airports
WHERE city = 'Fiftyville') AND hour = (SELECT MIN(hour) FROM flights
WHERE day = 29 AND month = 7 AND year = 2020 AND origin_airport_id = (SELECT id FROM airports
WHERE city = 'Fiftyville'));

-- Accomplice: To whom he called? Who is the receiver's name from that call?
SELECT name FROM people
WHERE phone_number IN (SELECT receiver FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60 AND caller IN (
    SELECT phone_number FROM people
    WHERE name = 'Ernest'
));