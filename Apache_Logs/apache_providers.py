#!/usr/bin/python
from faker.providers import DynamicProvider

# in the loggen file:
# fake = Faker()    >> establish faker instance and
# fake.add_provider(random_email)    >> add custom providers to the instance by importing them in the loggen file
# fake.random_email  >> make a call to the provider to generate random value

private_ipv4 = DynamicProvider(
     provider_name="private_ipv4",
     elements=["192.168.76.113",
        "10.101.119.103",
        "192.168.155.252",
        "172.23.103.67",
        "192.168.246.213",
        "10.219.133.182",
        "192.168.162.71",
        "172.26.38.103",
        "10.215.157.105",
        "192.168.9.220",
        "192.168.150.2",
        "192.168.33.199",
        "192.168.150.31",
        "192.168.252.120",
        "172.25.52.57",
        "10.42.182.103",
        "172.19.173.2",
        "10.194.135.159",
        "172.31.115.98",
        "10.223.245.56"]
)

public_ipv4 = DynamicProvider(
     provider_name="public_ipv4",
     elements=["24.107.254.35",
        "90.104.3.103",
        "130.251.2.21",
        "214.233.124.129",
        "193.91.159.123",
        "169.220.235.127",
        "183.169.115.55",
        "137.99.235.200",
        "60.101.118.73",
        "165.204.207.53",
        "9.115.186.197",
        "180.248.75.125",
        "66.126.203.15",
        "212.74.11.54",
        "110.126.105.117",
        "133.70.158.39",
        "176.6.89.88",
        "194.123.200.131",
        "142.52.214.246",
        "185.26.247.72"]
)

status_code = DynamicProvider(
     provider_name="status_code",
     elements=["200",
        "202",
        "301",
        "303",
        "307",
        "401",
        "403",
        "404",
        "500",
        "502"]
)

method = DynamicProvider(
     provider_name="method",
     elements=["GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"]
)

uri = DynamicProvider(
     provider_name="uri",
     elements=["/tags/explore/homepage.html",
        "/app/search/tag/terms.html",
        "/index/",
        "/list/tag/wp-content/terms/",
        "/privacy.jsp",
        "/gonzalez-tucker.net/",
        "/home.php",
        "/posts/faq.asp",
        "/category/home/",
        "/search/wp-content/wp-content/author.html",
        "/search.html",
        "/wp-content/register/",
        "/login/",
        "/search/category/search/",
        "/explore/app/app/main.html",
        "/main/categories/blog/privacy/"]
)

user_agent = DynamicProvider(
     provider_name="user_agent",
     elements=["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/53.0.832.0 Safari/531.2",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/535.0 (KHTML, like Gecko) CriOS/23.0.806.0 Mobile/36D600 Safari/535.0",
        "Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.19.4 (KHTML, like Gecko) Version/4.1 Safari/532.19.4",
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/32.0.801.0 Safari/531.2",
        "Mozilla/5.0 (Linux; Android 2.3) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/25.0.861.0 Safari/533.1",
        "Opera/8.74.(X11; Linux x86_64; fi-FI) Presto/2.9.188 Version/12.00",
        "Mozilla/5.0 (Linux; Android 3.2.1) AppleWebKit/536.2 (KHTML, like Gecko) Chrome/40.0.869.0 Safari/536.2",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 3_0 like Mac OS X; tn-ZA) AppleWebKit/535.18.5 (KHTML, like Gecko) Version/3.0.5 Mobile/8B113 Safari/6535.18.5",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.01; Trident/3.1)",
        "Opera/8.24.(X11; Linux i686; lv-LV) Presto/2.9.163 Version/11.00"]
)

filepath = DynamicProvider(
     provider_name="filepath",
     elements=["var/log/",
        "system/",
        "syslog/server1/",
        "syslog/server2/",
        "syslog/server3/",
        "application/mobile/",
        "application/web/"]
)

bytes = DynamicProvider(
     provider_name="bytes",
     elements=[654,
        142,
        94,
        389,
        2609]
)