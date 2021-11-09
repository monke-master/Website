UPDATE users SET registration_date = SUBSTR(registration_date, 7, 4) || '-' || SUBSTR(registration_date, 4, 2) || '-' ||
SUBSTR(registration_date, 1, 2);