Match a string that contains no spaces<start>import re; re.match(r'^\S+$', 'NoSpacesHere')<end>

Match a string that contains a specific word at the beginning<start>import re; re.match(r'^Word\b', 'Word of the day')<end>

Match a string that is a valid Python identifier<start>import re; re.match(r'^[a-zA-Z_]\w*$', '_variable')<end>

Match a string that contains a valid HTML hex color code<start>import re; re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', '#ABC123')<end>

Match a string that contains a valid 12-hour time format with AM/PM<start>import re; re.match(r'^(0[1-9]|1[0-2]):[0-5]\d (AM|PM)$', '10:30 AM')<end>

Match a string that contains a valid 4-digit PIN<start>import re; re.match(r'^\d{4}$', '1234')<end>

Match a string that contains no consonants<start>import re; re.match(r'^[aeiouAEIOU]+$', 'aeiou')<end>

Match a string that contains a valid CVV (3 or 4 digits)<start>import re; re.match(r'^\d{3,4}$', '123')<end>

Match a string that contains no digits<start>import re; re.match(r'^\D+$', 'abcdef')<end>

Match a string that starts with a number<start>import re; re.match(r'^\d', '123abc')<end>

Match a string that contains a specific character repeated multiple times<start>import re; re.match(r'^[a]{5}$', 'aaaaa')<end>

Match a string that contains a repeated word<start> import re; re.search(r'\b(\w+)\s+\1\b', 'word word')<end>

Match a string that contains a number greater than 100<start>import re; re.match(r'^(1\d{2,}|[2-9]\d{2,}|\d{4,})$', '150')<end>

Match a floating-point number<start>import re; re.match(r'^\d+\.\d+$', '123.456')<end>

Match a string that is a valid time duration in HH:MM format<start>import re; re.match(r'^\d{2}:\d{2}:\d{2}$', '12:34:56')<end>

Match a string that is a valid ISBN-10<start>import re; re.match(r'^\d{9}[0-9Xx]$', '123456789X')<end>

Match a string that ends with a period<start>import re; re.match(r'.*\.$', 'This is a sentence.')<end>

Match a string that contains a valid percentage (0-100%)<start>import re; re.match(r'^(100|[1-9]?[0-9])%$', '99%')<end>

Match a string that contains at least one lowercase letter<start>import re; re.search(r'[a-z]', 'Hello')<end>

Match a string that contains two identical consecutive words<start>import re; re.search(r'\b(\w+)\s+\1\b', 'word word')<end>

Match a string that is a valid integer<start>import re; re.match(r'^\d+$', '12345')<end>

Match a string that contains the same word three times<start>import re; re.search(r'\b(\w+)\b.*\b\1\b.*\b\1\b', 'word word word')<end>

Match a hex color code<start>import re; re.match(r'#[0-9a-fA-F]{6}', '#a3c113')<end>

Match a date in YYYY-MM-DD format<start>import re; re.match(r'\d{4}-\d{2}-\d{2}', '2024-09-01')<end>

Match a string that contains a valid CVC code (3 digits)<start>import re; re.match(r'^\d{3}$', '123')<end>

Match a string that is a valid floating-point number<start>import re; re.match(r'^[-+]?[0-9]*\.?[0-9]+$', '3.14')<end>

Match a string that contains a valid binary number<start>import re; re.match(r'^[01]+$', '1101')<end>

Match a string that contains a valid 24-hour time format<start>import re; re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', '23:45')<end>

Match a string that is exactly 10 characters long<start>import re; re.match(r'^.{10}$', 'abcdefghij')<end>

Match a string containing only digits<start>import re; re.match(r'^\d+$', '123456')<end>

Match a valid IPv4 address<start>import re; re.match(r'(\d{1,3}\.){3}\d{1,3}', '192.168.1.1')<end>

Match a string that contains only whitespace characters<start>import re; re.match(r'^\s+$', '    ')<end>

Match a string that contains a valid date in DD/MM/YYYY format<start>import re; re.match(r'^\d{2}/\d{2}/\d{4}$', '01/09/2024')<end>

Match a string that contains a valid email address with a specific domain<start>import re; re.match(r'^[\w\.-]+@example\.com$', 'user@example.com')<end>

Match a string that contains a valid 3-letter ISO country code<start>import re; re.match(r'^[A-Z]{3}$', 'USA')<end>

Match a string that contains a valid vehicle license plate number<start>import re; re.match(r'^[A-Z0-9]{1,7}$', 'ABC1234')<end>

Match a string that contains a valid simple mathematical expression<start>import re; re.match(r'^\d+[\+\-\*\/]\d+$', '3+5')<end>

Match a valid Twitter handle<start>import re; re.match(r'^@(\w{1,15})$', '@username')<end>

Match a string that is a valid file path<start>import re; re.match(r'^(/[^/ ]*)+/?$', '/home/user/file.txt')<end>

Match a string that contains only lowercase letters<start>import re; re.match(r'^[a-z]+$', 'abcdef')<end>

Match a string that contains a valid fraction<start>import re; re.match(r'^\d+/\d+$', '1/2')<end>

Match a string that contains a word that starts with a capital letter<start>import re; re.search(r'\b[A-Z][a-z]*\b', 'Hello World')<end>

Match a string that contains a valid file extension<start>import re; re.match(r'^.+\.(jpg|jpeg|png|gif)$', 'image.jpg')<end>

Match a U.S. zip code (5 or 9 digits)<start>import re; re.match(r'\d{5}(-\d{4})?', '12345-6789')<end>

Match a string that contains no vowels<start>import re; re.match(r'^[^aeiouAEIOU]+$', 'bcdfg')<end>

Match a string that is a palindrome<start>import re; re.match(r'^(?P<word>.+)(?P=word[::-1])$', 'radar')<end>

Match a valid HTML tag<start>import re; re.match(r'^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$', '<div>content</div>')<end>

Match a valid email address<start>import re; re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', 'example@example.com')<end>

Match a string that contains a number with exactly two decimal places<start>import re; re.match(r'^\d+\.\d{2}$', '123.45')<end>

Match a string that contains a specific number of digits<start> import re; re.match(r'^\d{6}$', '123456')<end>

Match a string that contains "cat" or "dog"<start>import re; re.search(r'cat|dog', 'I have a cat')<end>

Match a string that contains a valid hexadecimal number<start>import re; re.match(r'^[0-9a-fA-F]+$', '1A3F')<end>

Match a string that ends with "xyz"<start>import re; re.match(r'xyz$', '123xyz')<end>

Match a valid MAC address<start>import re; re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', '01:23:45:67:89:AB')<end>

Match a string that is a valid US dollar amount<start>import re; re.match(r'^\$\d+(\.\d{2})?$', '$100.00')<end>

Match a string that contains a valid hexadecimal color code<start>import re; re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', '#fff')<end>

Match a time in HH format<start>import re; re.match(r'\d{2}:\d{2}', '14:30')<end>

Match a valid credit card number (16 digits)<start>import re; re.match(r'\d{4}-?\d{4}-?\d{4}-?\d{4}', '1234-5678-9876-5432')<end>

Match a string that contains a valid hexadecimal string<start>import re; re.match(r'^[A-Fa-f0-9]+$', '1A3F')<end>

Match a string containing only letters<start>import re; re.match(r'^[a-zA-Z]+$', 'abcDEF')<end>

Match a string that is a valid ISBN-13<start>import re; re.match(r'^\d{13}$', '9781234567897')<end>

Match a valid domain name<start>import re; re.match(r'^[a-zA-Z0-9-]{1,63}\.[a-zA-Z]{2,}$', 'example.com')<end>

Match a string that contains a valid UUID<start>import re; re.match(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', '123e4567-e89b-12d3-a456-426614174000')<end>

Match a string that contains any non-word character<start>import re; re.search(r'\W', 'hello@world')<end>

Match a string that contains a valid floating-point number with a sign<start>import re; re.match(r'^[+-]?\d+\.\d+$', '-123.45')<end>

Match a string that contains only uppercase letters<start>import re; re.match(r'^[A-Z]+$', 'ABCDEF')<end>

Match a string that contains a specific word at the end<start>import re; re.match(r'.*\bWord$', 'End with Word')<end>

Match a string that contains a valid variable name (letters, digits, underscores)<start>import re; re.match(r'^[a-zA-Z_]\w*$', 'variable_name')<end>

Match a string that contains "apple" followed by "pie"<start>import re; re.search(r'apple.*pie', 'apple and pie')<end>

Match a string that contains a valid ISBN<start>import re; re.match(r'^(\d{9}[\dXx]|\d{13})$', '123456789X')<end>

Match a string that contains a valid HTML tag with attributes<start>import re; re.match(r'^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$', '<img src="image.jpg" />')<end>

Match a string that contains only printable ASCII characters<start>import re; re.match(r'^[\x20-\x7E]+$', 'Hello, World!')<end>

Match a string that contains a valid floating-point number (including optional +, -, .)<start>import re; re.match(r'^[-+]?\d*\.\d+$', '123.45')<end>

Match a string that contains at least one digit<start>import re; re.search(r'\d', 'abc123')<end>

Match a string that contains exactly 3 letters<start>import re; re.match(r'^[a-zA-Z]{3}$', 'abc')<end>

Match a string that starts with "abc"<start>import re; re.match(r'^abc', 'abc123')<end>

Match a string that contains a valid hex digit<start>import re; re.match(r'^[0-9A-Fa-f]+$', '1A3F')<end>

Match a string that contains any whitespace character<start>import re; re.search(r'\s', 'Hello World')<end>

Match a string that contains a valid social security number (XXX-XX-XXXX)<start>import re; re.match(r'\d{3}-\d{2}-\d{4}', '123-45-6789')<end>

Match a string that contains at least one special character<start>import re; re.search(r'[^a-zA-Z0-9]', 'hello@world')<end>

Match a string that contains no special characters<start>import re; re.match(r'^[a-zA-Z0-9]+$', 'NoSpecialChars')<end>

Match a string that contains only alphanumeric characters<start>import re; re.match(r'^[a-zA-Z0-9]+$', 'abc123')<end>

Match a string that contains at least one vowel<start>import re; re.search(r'[aeiouAEIOU]', 'hello')<end>

Match a string that contains at least one uppercase letter<start>import re; re.search(r'[A-Z]', 'Hello')<end>

Match a string that contains a valid time in HH:MM format<start>import re; re.match(r'^\d{2}:\d{2}:\d{2}$', '14:30:59')<end>

Match a valid Instagram handle<start>import re; re.match(r'^@(\w{1,30})$', '@username')<end>

Match a string that contains a valid phone number with country code<start>import re; re.match(r'^\+\d{1,3}\s\d{10}$', '+1 1234567890')<end>

Match a string that contains at least one uppercase and one lowercase letter<start>import re; re.match(r'^(?=.*[a-z])(?=.*[A-Z]).+$', 'HelloWorld')<end>

Match a string containing both letters and digits<start>import re; re.match(r'^[a-zA-Z0-9]+$', 'abc123')<end>

Match a valid URL<start>import re; re.match(r'https?://[^\s/$.?#].[^\s]*', 'https://www.example.com')<end>

Match a U.S. phone number (XXX-XXX-XXXX)<start>import re; re.match(r'\d{3}-\d{3}-\d{4}', '123-456-7890')<end>

Match a string that contains a specific pattern repeated exactly n times<start> import re; re.match(r'^(abc){3}$', 'abcabcabc')<end>

Match a password with at least 8 characters, 1 digit, 1 uppercase, 1 lowercase<start>import re; re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', 'Passw0rd')<end>

Match a string that starts with a specific digit<start>import re; re.match(r'^[5-9]', '5abc')<end>

Match a string that contains a valid date in MM/DD/YYYY format<start>import re; re.match(r'^\d{2}/\d{2}/\d{4}$', '09/01/2024')<end>

Match a string that contains a date in YYYY/MM/DD format<start> import re; re.match(r'^\d{4}/\d{2}/\d{2}$', '2024/09/01')<end>

Match a string that contains any word longer than 10 characters<start>import re; re.search(r'\b\w{11,}\b', 'supercalifragilistic')<end>

Match a word boundary<start>import re; re.search(r'\bword\b', 'word boundary')<end>

Match a string that contains a valid Roman numeral<start>import re; re.match(r'^(M{0,4})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', 'MMXXIV')<end>

Match a string that contains a valid octal number<start>import re; re.match(r'^[0-7]+$', '1234567')<end>

