# Skrypt do Testowania API

## Opis

Ten skrypt jest przeznaczony do automatycznego testowania różnych endpointów API JSONPlaceholder za pomocą narzędzia `curl`. Wysyła żądania HTTP GET do wybranych endpointów, sprawdza kody statusów HTTP oraz weryfikuje obecność kluczowych elementów w odpowiedziach JSON.

## Wymagania

- Python 3.x
- Biblioteka `requests`

## Użycie

1. Upewnij się, że `curl` jest zainstalowany na Twoim systemie.
2. Zapisz skrypt jako `api_test.py`.
3. Uruchom skrypt za pomocą polecenia:
    ```sh
    python api_test.py
    ```

## Testowane Endpointy

Skrypt testuje następujące endpointy API JSONPlaceholder:

1. GET /posts/1

Oczekiwany kod statusu: 200
Klucze: userId, id, title, body

2. GET /users/1

Oczekiwany kod statusu: 200
Klucze: id, name, username, email

3. GET /todos/1

Oczekiwany kod statusu: 200
Klucze: userId, id, title, completed

## Przykładowy Wynik

Test 1: PASSED
Test 2: PASSED
Test 3: PASSED

## Autor

- Wiktor Brzeziński