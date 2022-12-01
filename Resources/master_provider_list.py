from faker.providers import DynamicProvider

# in the loggen files:
# fake = Faker()    >> establish faker instance and
# fake.add_provider(random_email)    >> add custom providers to the instance by importing them in the loggen file
# fake.random_email  >> make a call to the provider to generate random value

email = DynamicProvider(
     provider_name="email",
     elements=["bob.smith@cigolomus.com",
        "bob_smith@cigolomus.com",
        "jane.doe@cigolomus.com",
        "jane.doe@gmail.com",
        "richardprice@cigolomus.com",
        "richardprice@gmail.com",
        "richard_prce@yahoo.com",
        "anthony@cigolomus.com",
        "marylou@cigolomus.com",
        "evan.wright4@cigolomus.com",
        "evan4wright@gmail.com",
        "chelsea_hans@cigolomus.com",
        "victor.manny@yahoo.com",
        "chris.wentworth@cigolomus.com",
        "jordan.lamb@cigolomus.com",
        "jordan_lamb@gmail.com",
        "tyler_freeze@cigolomus.com",
        "kristen@cigolomus.com",
        "kristen@yahoo.com",
        "support@cigolomus.com"]
)

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

ipv6 = DynamicProvider(
     provider_name="ipv6",
     elements=["d396:309e:c2ad:945b:7053:afb2:7728:5619",
        "c351:d46e:f59d:7a31:f08f:c27d:8292:43fa",
        "1ab9:3a4c:41c3:8472:558e:861c:f784:1b6",
        "2be1:3d1a:150a:89aa:e0f1:353c:48e0:42ee",
        "a6d3:c3fc:6a18:5e7f:b5de:1583:18da:7f8b",
        "cc02:688d:d524:c870:85cd:52c4:bce:694",
        "60af:7cad:60e3:9503:f424:dbf4:7cd2:fb15",
        "63d5:a739:9d9a:8961:59d2:cfe2:d3ca:6487",
        "fd72:7f66:38d3:c1c3:8444:aacc:d487:2b70",
        "e943:f1b4:e554:acb5:3e5:d2af:58a7:387c"]
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

filename = DynamicProvider(
     provider_name="filename",
     elements=["hospital.avi",
        "pass.wav",
        "benefit.csv",
        "minute.tiff",
        "newspaper.mp4",
        "something.webm",
        "factor.odp",
        "quickly.avi",
        "drive.pdf",
        "no.webm",
        "fine.css",
        "popular.json",
        "big.ods",
        "specific.odt",
        "home.txt",
        "participant.mp4",
        "medical.numbers",
        "southern.json",
        "use.jpeg",
        "away.gif"]
)

port = DynamicProvider(
     provider_name="port",
     elements=[ 1227,
        13401,
        2727,
        35738,
        29730,
        35838,
        17098,
        32189,
        49104,
        47476,
        443,
        22,
        8080,
        8888]
)

mac_address = DynamicProvider(
     provider_name="mac_address",
     elements=["79:4b:ce:73:e1:2c",
        "a0:a1:65:5e:72:49",
        "0f:b0:5c:f0:fc:ff",
        "17:91:68:cd:db:64",
        "85:d4:13:c6:10:29",
        "3e:94:1a:ba:73:a4",
        "27:19:da:9e:e7:69",
        "32:96:96:53:8e:5a",
        "d0:13:0d:78:d9:52",
        "60:2c:c6:28:de:0f"]
)

level = DynamicProvider(
     provider_name="level",
     elements=["info",
        "debug",
        "warning",
        "error"]
)

severity_int = DynamicProvider(
     provider_name="severity_int",
     elements=[1,
        3,
        6,
        9,
        10]
)

severity_text = DynamicProvider(
     provider_name="severity_text",
     elements=["low",
        "medium",
        "high",
        "critical"]
)

bytes = DynamicProvider(
     provider_name="bytes",
     elements=[654,
        142,
        94,
        389,
        2609]
)