from faker.providers import DynamicProvider

## in the loggen file, establish faker instance:
# fake = Faker()

## add custom providers to the instance by importing them in the loggen file
# fake.add_provider(email)

## make a call to a provider to generate random value from the list in the provider
# fake.email

bytes = DynamicProvider(
     provider_name="bytes",
     elements=[654,
        142,
        94,
        389,
        2609]
)

cve = DynamicProvider(
     provider_name="cve",
     elements=[
       "CVE-2022-32221",
       "CVE-2022-35260",
       "CVE-2022-42915",
       "CVE-2022-42916",
       "CVE-2022-29526",
       "CVE-2022-30629",
       "CVE-2022-30633",
       "CVE-2022-30635",
       "CVE-2022-30630",
       "CVE-2022-1996",
       "CVE-2022-28327",
       "CVE-2022-1962",
       "CVE-2022-32148",
       "CVE-2022-30631",
       "CVE-2022-28131",
       "CVE-2022-27191",
       "CVE-2022-30632",
       "CVE-2022-1705",
       "CVE-2022-24675"  
     ]
)

device_type = DynamicProvider(
     provider_name="device_type",
     elements=["printer",
     "router",
     "general-purpose",
     ]
)

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

fqdn = DynamicProvider(
     provider_name="fqdn",
     elements=[
        "web-66.green.info",
        "laptop-47.silva-odonnell.net",
        "srv-42.montgomery.net",
        "email-92.garcia-jones.com",
        "laptop-81.hamilton-carr.com",
        "lt-77.green.com",
        "db-60.snyder.com",
        "email-13.walker.net",
        "laptop-11.golden-bolton.info",
        "db-48.mann-kelley.net",
        "maynard.net",
        "roberts.com",
        "allen.com",
        "zavala.com",
        "mclean.net",
        "myers.com",
        "jacobson.biz",
        "hill.com",
        "nguyen.info",
        "mccoy.com",
        "maryannes-macbook-pro.local",
        "jalee-macbook-pro.local",
        "max-macbook-pro.local",
        "duncan-macbook-pro.local",
        "david-macbook-pro.local",
        "patrick-macbook-pro.local",
        "rob-macbook-pro.local",
     ]
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

level = DynamicProvider(
     provider_name="level",
     elements=["info",
        "debug",
        "warning",
        "error"]
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

method = DynamicProvider(
     provider_name="method",
     elements=["GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"]
)

operating_sys = DynamicProvider(
     provider_name="operating_sys",
     elements=[
          "Macintosh; U; PPC Mac OS X 10_11_0",
          "Macintosh; U; Intel Mac OS X 10_12_6",
          "Macintosh; U; Intel Mac OS X 10_12_5",
          "Macintosh; PPC Mac OS X 10_7_4",
          "Macintosh; PPC Mac OS X 10_6_9",
          "Macintosh; U; Intel Mac OS X 10_7_4",
          "Macintosh; Intel Mac OS X 10_6_5",
          "Macintosh; U; PPC Mac OS X 10_6_5",
          "Macintosh; U; PPC Mac OS X 10_10_9",
          "Macintosh; PPC Mac OS X 10_12_7",
          "Windows NT 5.2",
          "Windows NT 4.0",
          "Windows 95",
          "Windows NT 10.0",
          "Windows 98",
          "Windows NT 6.2",
          "Windows NT 5.01",
          "X11; Linux x86_64",
          "X11; Linux i686"
     ]
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

protocol = DynamicProvider(
     provider_name="protocol",
     elements=[
          "TCP",
          "UDP"
          ]
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

risk = DynamicProvider(
     provider_name="risk",
     elements=[
          "Critical",
          "High",
          "Medium",
          "Low",
          "None"
     ]
)

severity_int = DynamicProvider(
     provider_name="severity_int",
     elements=[0,
        1,
        2,
        3,
        4,
        5]
)

severity_text = DynamicProvider(
     provider_name="severity_text",
     elements=["low",
        "medium",
        "high",
        "critical"]
)

status = DynamicProvider(
     provider_name="status",
     elements=[
          "OPEN",
          "REOPENED",
          "CLOSED"
          ]
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

vulnerability_name = DynamicProvider(
     provider_name="vulnerability_name",
     elements=[
          "Injection",
          "Broken Authentication",
          "Sensitive Data Exposure",
          "XML External Entities",
          "Broken Access Control",
          "Security Misconfiguration",
          "Cross-Site Scripting",
          "Insecure Deserialization",
          "Using Components with Known Vulnerabilities",
          "Insufficient Logging and Monitoring"
     ]
)

agent_uuid = DynamicProvider(
     provider_name="agent_uuid",
     elements=[
        "b2887c7c781411eda1eb0242ac120002",
        "b2888122781411eda1eb0242ac120002",
        "b288826c781411eda1eb0242ac120002",
        "b28883a2781411eda1eb0242ac120002",
        "b28884b0781411eda1eb0242ac120002",
        "b28888ca781411eda1eb0242ac120002",
        "b2888a46781411eda1eb0242ac120002",
        "b2888bd6781411eda1eb0242ac120002",
        "b2888d20781411eda1eb0242ac120002",
        "b2888e24781411eda1eb0242ac120002",
        "b28890c2781411eda1eb0242ac120002",
        "b2889220781411eda1eb0242ac120002",
        "b2889694781411eda1eb0242ac120002",
        "b28897ac781411eda1eb0242ac120002",
        "b28898a6781411eda1eb0242ac120002",
        "b2889a04781411eda1eb0242ac120002",
        "b2889b12781411eda1eb0242ac120002",
        "b2889ce8781411eda1eb0242ac120002",
        "b2889e0a781411eda1eb0242ac120002",
        "b288a99a781411eda1eb0242ac120002",
        "b288ab2a781411eda1eb0242ac120002",
        "b288aca6781411eda1eb0242ac120002",
        "b288ae04781411eda1eb0242ac120002",
        "b288af62781411eda1eb0242ac120002",
        "b288b07a781411eda1eb0242ac120002",
        "b288b192781411eda1eb0242ac120002",
        "b288b4b2781411eda1eb0242ac120002",
        "b288b5de781411eda1eb0242ac120002",
        "b288b6f6781411eda1eb0242ac120002",
        "b288b804781411eda1eb0242ac120002",
        "b288ba52781411eda1eb0242ac120002",
        "b288bb7e781411eda1eb0242ac120002",
        "b288bca0781411eda1eb0242ac120002",
        "b288bda4781411eda1eb0242ac120002",
        "b288c0d8781411eda1eb0242ac120002",
        "b288c1e6781411eda1eb0242ac120002",
        "b288c308781411eda1eb0242ac120002",
        "b288c42a781411eda1eb0242ac120002",
        "b288c542781411eda1eb0242ac120002",
        "b288c664781411eda1eb0242ac120002",
        "b288c768781411eda1eb0242ac120002",
        "b288cae2781411eda1eb0242ac120002",
        "b288cc0e781411eda1eb0242ac120002",
        "b288cd12781411eda1eb0242ac120002",
        "b288ce52781411eda1eb0242ac120002",
        "b288cfc4781411eda1eb0242ac120002",
        "b288d0f0781411eda1eb0242ac120002",
        "b288d1f4781411eda1eb0242ac120002",
        "b288d9c4781411eda1eb0242ac120002"
     ]
)

uuid = DynamicProvider(
     provider_name="uuid",
     elements=[
        "09c78e8d-9702-46f1-9b25-8bd277eda275",
        "b3ca7437-2e5f-4526-a5f3-89fd850fa798",
        "d5ff6e94-ca6d-4338-acca-ba00f21d39b2",
        "0e3cfd09-420f-401f-bda5-d3a8eee38cd3",
        "e5cb4133-ab35-4595-8772-ae7f9cdd4a33",
        "59837ae2-851e-4f06-bdcd-4943d492e2e1",
        "c1db1906-148d-4512-9528-636b5837c3a4",
        "f3128ab5-48fa-42a8-8a40-da8a16826f49",
        "b8fa7e62-aaeb-4310-bd6f-2898d5ba548e",
        "1cc42758-ec9d-4537-b808-f0d2babcdbb4",
        "7c2b0a9f-763c-4e17-868b-e4509b9ffc95",
        "a7c46515-bc25-4c22-af88-d25f1af760d5",
        "2d210e01-0322-4b39-be10-2b57e644f7d5",
        "f055787a-66b9-43e1-8870-073be3c31c98",
        "9889ddaf-77e5-42ef-a2e1-10b8d81f4a40",
        "b973d20c-c45c-4fc6-bbce-f172d28dfd90",
        "e22f3981-67f4-499f-bbe4-682cc405400d",
        "a7c5ce7f-e84b-4aab-b696-2b13f2f0a2c1",
        "5a5895f3-f390-4e77-99f8-648577caa78e",
        "b8f39b69-0eaa-4798-8fde-3f4e50ad84c7",
        "74b2a47b-d7c5-4ef2-ad93-3a4cecb762a7",
        "1d2ab13a-eacb-4194-9f81-038461626aa5",
        "ab922d7a-513f-48b5-888e-28f7e6f64478",
        "d3f2b948-c840-4806-aed3-ea5841ac8311",
        "847f07a4-7bd6-434d-be40-4548c23f5998",
        "4af84130-e70e-4a8f-a4d1-3e393130d957",
        "5eb03d83-e0f2-488e-b4f7-2180636998f2",
        "c94e25d0-3890-4f65-82c6-edca36d25ed7",
        "4d0edcae-ce3c-4265-b7d3-ce2b1ed1c35f",
        "d65a5669-d40e-45e6-bb14-be1572325851",
        "cfb20e25-4efc-492e-9189-138787f04356",
        "31b357b3-850f-4140-8826-44a4239e0a5e",
        "0fb786cb-9e50-4217-8c4d-ce022db4b64f",
        "23727e2b-cef3-4ad6-b47a-9f70e3ac698a",
        "4b41a9f3-a6e7-44b0-a7f0-e577b3879582",
        "b974142b-6ee5-42a3-a51b-bcbdba9fd77a",
        "d0cc5f23-da58-4d4b-9b0f-1f39bcdb7838",
        "3957e4ce-92ee-4513-8f7b-1bab62c42728",
        "d37cf9b8-fb10-4b17-9aeb-c106f55fdb07",
        "f6b5891e-ff6a-4a1f-82bf-6c8908d23099",
        "d5a0ed17-86f9-4b7a-b412-3cc797424bc3",
        "34464fa5-9e62-4695-bb66-ef9f23a9220b",
        "ba0fe3aa-2905-4223-8e3b-ed8c9ebe2d5e",
        "185a23ca-c4aa-4b8e-98ce-e20d0b38bde8",
        "5b9a5eb0-b08d-4012-97de-e7cbf3e5f913",
        "4f32c56e-69d4-4d8e-bf1e-0bc8c8b6f2e8",
        "c7aa0632-120c-45fe-b561-ee48f9d45bec",
        "12e1574e-8ae0-4655-909a-84dc6dbc4f43",
        "9feadf5a-8909-454d-889f-e7cf5e83c366",
        "f570f609-7cf5-4ef9-a4fb-3c5f5dcf4abb",
        "b708f543-2a79-485c-bfdc-bd2f9fbdedf4",
        "8a559495-5546-4c56-bb8b-3bfc7ef00898",
        "4fec8703-90f4-4c52-b181-ae76cbcd3d6a",
        "3d1977a3-ab53-48ce-8311-0cef5c0bd027",
        "791cac7e-4f70-4dd3-abf0-8045913fcfa7",
        "5b0d0ee1-1d69-4434-bf24-400f1939c410",
        "cfea9943-979a-4f7c-9da8-c9bf72eb7060",
        "bffc4f60-9644-48ed-94ed-b58f19e46fd8",
        "2b686fbc-7b43-4ddb-9df1-53d979918c99",
        "13e52e03-68cf-4ef8-9c91-46aecebb7d3f",
        "1291bd53-aaa2-46f8-ac3c-9d257bcc8ca2",
        "a844631f-e3bd-4696-bf57-90e534f1fae2",
        "a3e56a51-ab32-4ea7-93b3-c963d4f24c6e",
        "05357d64-86e4-4699-83ea-56a60820c3ae",
        "759ed64a-cda8-42bb-80f8-1998ec91b5cb",
        "8b8643bc-f83f-4757-a4cd-d3a820e344a4"
     ]
)