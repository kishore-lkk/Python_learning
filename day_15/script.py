from request_package import response, headers, cookies

print(response("https://github.com"))
print(headers("https://github.com"))
print(cookies("https://github.com"))