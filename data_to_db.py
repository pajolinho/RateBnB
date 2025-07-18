from app import db, Bnb, app

with app.app_context():
    db.create_all()
    entries = [
        Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-1448392717596005579/original/2d859c0c-c2d6-4527-b327-5a2602114524.jpeg?im_w=1200",
            title="Tiny House in Kvášňovice, Tschechien",
            location="Kvášňovice, Tschechien",
            beds=1,
            rooms=1,
            price_per_night=124,
            link="https://www.airbnb.de/rooms/1448392717596005579?search_mode=regular_search&adults=1&category_tag=Tag%3A8144&check_in=2025-07-06&check_out=2025-07-11&children=0&infants=0&pets=0&photo_id=2222512369&source_impression_id=p3_1751221848_P3CS2aVEbzB0rn3n&previous_page_section_name=1000&federated_search_id=9afda000-75d3-468c-ab26-96a42892c8e1"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTQyMTg2NTkzNzc1NzEwMjcxNw==/original/f759dfc2-966a-4d86-ae48-68f365869528.jpeg?im_w=1200",
            title="Hütte in Erlenbach im Simmental, Schweiz",
            location="Erlenbach im Simmental, Schweiz",
            beds=1,
            rooms=1,
            price_per_night=103,
            link="https://www.airbnb.de/rooms/1421865937757102717?search_mode=regular_search&adults=1&check_in=2025-08-28&check_out=2025-09-02&children=0&infants=0&pets=0&source_impression_id=p3_1751221848_P3dl6SV_VajjNaGZ&previous_page_section_name=1000&federated_search_id=9afda000-75d3-468c-ab26-96a42892c8e11"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6NjI1MDM1NjE1NTc1NTc4MDQ1/original/6b552f68-5bbc-44b8-8d67-e7e01448c486.jpeg?im_w=1200",
            title="Zelt in Jubbega, Niederlande",
            location="Jubbega, Niederlande",
            beds=1,
            rooms=1,
            price_per_night=86,
            link="https://www.airbnb.de/rooms/625035615575578045?search_mode=regular_search&adults=1&category_tag=Tag%3A8102&check_in=2025-07-01&check_out=2025-07-06&children=0&infants=0&pets=0&photo_id=2147558673&source_impression_id=p3_1751221848_P31Ec1FJToU6b6LJ&previous_page_section_name=1000&federated_search_id=9afda000-75d3-468c-ab26-96a42892c8e1"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTA5NDI5MTc3MjcxMDY4NDEyMw%3D%3D/original/c2b0ad41-2c07-492e-a1b9-fdd786c67621.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Apartment in Romainville, Frankreich",
            location="Romainville, Frankreich",
            beds=1,
            rooms=1,
            price_per_night=65,
            link="https://www.airbnb.de/rooms/1094291772710684123?search_mode=regular_search&adults=1&category_tag=Tag%3A8661&check_in=2025-11-22&check_out=2025-11-27&children=0&infants=0&pets=0&photo_id=1853689507&source_impression_id=p3_1751221848_P3jc3if5A7Z_CGQs&previous_page_section_name=1000&federated_search_id=9afda000-75d3-468c-ab26-96a42892c8e1"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-1447563731294396268/original/53224c35-269e-49c7-bd02-b84518301269.jpeg?im_w=1200",
            title="Tiny House in Stróża, Polen",
            location="Stróża, Polen",
            beds=3,
            rooms=1,
            price_per_night=38,
            link="https://www.airbnb.de/rooms/1447563731294396268?search_mode=regular_search&adults=1&check_in=2025-07-01&check_out=2025-07-06&children=0&infants=0&pets=0&source_impression_id=p3_1751221848_P3I_vCEEB7zLiS8a&previous_page_section_name=1000&federated_search_id=9afda000-75d3-468c-ab26-96a42892c8e1"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/ccd4a2f7-9345-4a4e-99d9-c43f84011a51.jpg?im_w=1200",
            title="Gesamte Unterkunft: Privatunterkunft in Dervio, Italien",
            location="Dervio, Italien",
            beds=2,
            rooms=1,
            price_per_night=160,
            link="https://www.airbnb.de/rooms/49671666?search_mode=regular_search&adults=1&category_tag=Tag%3A8536&check_in=2025-10-04&check_out=2025-10-09&children=0&infants=0&pets=0&photo_id=1389041019&source_impression_id=p3_1751221848_P359Awd2OUlpV-He&previous_page_section_name=1000&federated_search_id=9afda000-75d3-468c-ab26-96a42892c8e1"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/miso/Hosting-1446143117767803503/original/64faf0e2-e4a2-4394-bd82-b7a2f62ba362.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Privatunterkunft in Noordwijk, Niederlande",
            location="Noordwijk, Niederlande",
            beds=1,
            rooms=1,
            price_per_night=147,
            link="https://www.airbnb.de/rooms/1446143117767803503?search_mode=regular_search&adults=1&category_tag=Tag%3A8102&check_in=2025-07-05&check_out=2025-07-10&children=0&infants=0&pets=0&photo_id=2218127197&source_impression_id=p3_1751221848_P34sWNUdAGdtsVBc&previous_page_section_name=1000&federated_search_id=9afda000-75d3-468c-ab26-96a42892c8e1"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTQzOTY1OTA0OTg0MzA4MzgwNg==/original/7f51fce3-c668-4deb-a662-57174727e165.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Blockhütte in Ulcinj, Montenegro",
            location="Ulcinj, Montenegro",
            beds=1,
            rooms=1,
            price_per_night=86,
            link="https://www.airbnb.de/rooms/1439659049843083806?search_mode=regular_search&adults=1&check_in=2025-07-01&check_out=2025-07-06&children=0&infants=0&pets=0&source_impression_id=p3_1751221899_P3gmii0c0JwS8PXg&previous_page_section_name=1000&federated_search_id=2df3a152-9f5e-475a-9e3c-41964f062820"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/miso/Hosting-1033822242148976778/original/9cafcc00-a07e-4347-be1e-ebe228e4f953.jpeg?im_w=1200",
            title="Hausboot in Kortenhoef, Niederlande",
            location="Kortenhoef, Niederlande",
            beds=2,
            rooms=1,
            price_per_night=181,
            link="https://www.airbnb.de/rooms/1033822242148976778?search_mode=regular_search&adults=1&category_tag=Tag%3A8176&check_in=2025-07-06&check_out=2025-07-11&children=0&infants=0&pets=0&photo_id=1796447471&source_impression_id=p3_1751221899_P3nFdYmmtBTBfeHa&previous_page_section_name=1000&federated_search_id=2df3a152-9f5e-475a-9e3c-41964f062820"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-1415233876995002398/original/e242f023-8130-48b8-b3e2-f3e78c23820b.png?im_w=1200",
            title="Gesamte Unterkunft: Privatunterkunft in Livry-Gargan, Frankreich",
            location="Livry-Gargan, Frankreich",
            beds=1,
            rooms=1,
            price_per_night=169,
            link="https://www.airbnb.de/rooms/1415233876995002398?search_mode=regular_search&adults=1&category_tag=Tag%3A8144&check_in=2025-07-18&check_out=2025-07-23&children=0&infants=0&pets=0&photo_id=2198997994&source_impression_id=p3_1751221924_P3g-vtY_TTsrWh3B&previous_page_section_name=1000&federated_search_id=93c1711c-dccb-4099-a659-9bd8566b43a2"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/miso/Hosting-1403676077709572878/original/e136b830-7a06-48a7-a6ba-014a734721ef.png?im_w=1200",
            title="Gesamte Unterkunft: Villa in Carini, Italien",
            location="Carini, Italien",
            beds=1,
            rooms=1,
            price_per_night=63,
            link="https://www.airbnb.de/rooms/1403676077709572878?search_mode=regular_search&adults=1&category_tag=Tag%3A4104&check_in=2025-09-09&check_out=2025-09-14&children=0&infants=0&pets=0&photo_id=2145540990&source_impression_id=p3_1751221924_P3OunDuhixcNq-UM&previous_page_section_name=1000&federated_search_id=93c1711c-dccb-4099-a659-9bd8566b43a2"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTQzMjM0OTUwNTI2OTQ1MzcyMQ==/original/c1ebf543-a1fe-4df3-a13c-68604cf1aef5.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Privatunterkunft in Rijssen, Niederland",
            location="Rijssen, Niederland",
            beds=1,
            rooms=1,
            price_per_night=101,
            link="https://www.airbnb.de/rooms/1432349505269453721?search_mode=regular_search&adults=1&category_tag=Tag%3A8102&check_in=2025-07-12&check_out=2025-07-17&children=0&infants=0&pets=0&photo_id=2223693925&source_impression_id=p3_1751221924_P3SFgGiZb_9yoBcj&previous_page_section_name=1000&federated_search_id=93c1711c-dccb-4099-a659-9bd8566b43a2"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-1153630737193987649/original/758bd37b-98e5-4394-8d6d-04a01e264bdb.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Apartment in Mondragon, Frankreich",
            location="Mondragon, Frankreich",
            beds=2,
            rooms=1,
            price_per_night=190,
            link="https://www.airbnb.de/rooms/1153630737193987649?search_mode=regular_search&adults=1&category_tag=Tag%3A677&check_in=2025-08-24&check_out=2025-08-29&children=0&infants=0&pets=0&photo_id=1926244396&source_impression_id=p3_1751221924_P3GcWlHAtKC37bdw&previous_page_section_name=1000&federated_search_id=93c1711c-dccb-4099-a659-9bd8566b43a2"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/miso/Hosting-1448687068467887515/original/19ecb78c-47e7-44c0-9c57-9dd9b282de0b.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Apartment in Krattigen, Schweiz",
            location="Krattigen, Schweiz",
            beds=1,
            rooms=1,
            price_per_night=196,
            link="https://www.airbnb.de/rooms/1448687068467887515?search_mode=regular_search&adults=1&category_tag=Tag%3A7765&check_in=2025-07-23&check_out=2025-07-28&children=0&infants=0&pets=0&photo_id=2223070322&source_impression_id=p3_1751221924_P3SwWsxVpOEZ2PPC&previous_page_section_name=1000&federated_search_id=93c1711c-dccb-4099-a659-9bd8566b43a2"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/miso/Hosting-1450590432256373539/original/7f7c3e50-425a-434a-b1ee-f5fde07f4d6a.jpeg?im_w=1200",
            title="Tiny House in Dąbki, Polen",
            location="Dąbki, Polen",
            beds=1,
            rooms=1,
            price_per_night=102,
            link="https://www.airbnb.de/rooms/1450590432256373539?search_mode=regular_search&adults=1&check_in=2025-07-04&check_out=2025-07-10&children=0&infants=0&pets=0&source_impression_id=p3_1751221952_P3i9hcBU1AfHFvgM&previous_page_section_name=1000&federated_search_id=77b5fad2-1e05-4b77-b621-849de8e51c1b"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTMxMDg3MTQxNTA1MTYzMjA0MA%3D%3D/original/9099385c-ffb1-49dc-94bb-617a014e44d1.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Apartment in Prata, Italien",
            location="Prata, Italien",
            beds=2,
            rooms=1,
            price_per_night=125,
            link="https://www.airbnb.de/rooms/1310871415051632040?search_mode=regular_search&adults=1&category_tag=Tag%3A8661&check_in=2025-10-02&check_out=2025-10-07&children=0&infants=0&pets=0&photo_id=2054245379&source_impression_id=p3_1751221952_P3jqvM-ygwhgH8R6&previous_page_section_name=1000&federated_search_id=77b5fad2-1e05-4b77-b621-849de8e51c1b"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/miso/Hosting-1422405488886379928/original/28e62bfa-daac-4ff3-b747-eb4c967922d9.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Gästesuite in Landsmeer, Niederlande",
            location="Landsmeer, Niederlande",
            beds=1,
            rooms=1,
            price_per_night=113,
            link="https://www.airbnb.de/rooms/1422405488886379928?search_mode=regular_search&adults=1&category_tag=Tag%3A8102&check_in=2025-07-01&check_out=2025-07-06&children=0&infants=0&pets=0&photo_id=2176068313&source_impression_id=p3_1751221951_P3ck_9SIDiw_eObM&previous_page_section_name=1000&federated_search_id=77b5fad2-1e05-4b77-b621-849de8e51c1b"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-1384067467930933566/original/14ddae91-1710-4110-9686-c50062e33d3d.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Privatunterkunft in Travo, Italien",
            location="Travo, Italien",
            beds=1,
            rooms=1,
            price_per_night=66,
            link="https://www.airbnb.de/rooms/1384067467930933566?search_mode=regular_search&adults=1&category_tag=Tag%3A4104&check_in=2025-07-07&check_out=2025-07-12&children=0&infants=0&pets=0&photo_id=2115936015&source_impression_id=p3_1751221952_P3a2TZyaUgZvAEMC&previous_page_section_name=1000&federated_search_id=77b5fad2-1e05-4b77-b621-849de8e51c1b"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/miso/Hosting-51461437/original/0beeb447-d2ce-454b-b99e-3472f4f612a0.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Apartment in Kraljevica, Kroatien",
            location="Kraljevica, Kroatien",
            beds=1,
            rooms=1,
            price_per_night=175,
            link="https://www.airbnb.de/rooms/51461437?search_mode=regular_search&adults=1&category_tag=Tag%3A8102&check_in=2025-07-07&check_out=2025-07-12&children=0&infants=0&pets=0&photo_id=1232874609&source_impression_id=p3_1751221952_P3GzTX-PSIqNWrIF&previous_page_section_name=1000&federated_search_id=77b5fad2-1e05-4b77-b621-849de8e51c1b"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/33523eef-a4df-424b-9185-3be9b6cd465c.jpg?im_w=1200",
            title="Gesamte Unterkunft: Privatunterkunft in Podgrađe (Omiš), Kroatien",
            location="Podgrađe (Omiš), Kroatien",
            beds=2,
            rooms=1,
            price_per_night=86,
            link="https://www.airbnb.de/rooms/35859466?search_mode=regular_search&adults=1&check_in=2025-08-11&check_out=2025-08-16&children=0&infants=0&pets=0&source_impression_id=p3_1751221952_P3xkgaqNuR4wdw_k&previous_page_section_name=1000&federated_search_id=77b5fad2-1e05-4b77-b621-849de8e51c1b"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTM0MzUyNjk5MzU5NTc4MTkxNQ==/original/81fbb2f6-fcc8-45bd-a424-fefed651e071.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Ferienunterkunft in Spiglia, Italien",
            location="Spiglia, Italien",
            beds=2,
            rooms=1,
            price_per_night=140,
            link="https://www.airbnb.de/rooms/1343526993595781915?search_mode=regular_search&adults=1&category_tag=Tag%3A8536&check_in=2025-07-06&check_out=2025-07-11&children=0&infants=0&pets=0&photo_id=2090122298&source_impression_id=p3_1751221983_P3zUAayWEQDIZrzL&previous_page_section_name=1000&federated_search_id=09b4df56-0cd6-4ae0-8106-85b46db748a5"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTQyMzcyNzk2MjY2OTI0MTM0MQ==/original/c1f3fcfe-325a-4837-806e-18604c1ada27.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Apartment in Sarandë, Albanien",
            location="Sarandë, Albanien",
            beds=2,
            rooms=1,
            price_per_night=112,
            link="https://www.airbnb.de/rooms/1423727962669241341?search_mode=regular_search&adults=1&category_tag=Tag%3A8102&check_in=2025-07-29&check_out=2025-08-03&children=0&infants=0&pets=0&photo_id=2196045925&source_impression_id=p3_1751221983_P3Iu_Nu2N6TWHejT&previous_page_section_name=1000&federated_search_id=09b4df56-0cd6-4ae0-8106-85b46db748a5"
        ),
         Bnb(
            image_url="https://a0.muscache.com/im/pictures/hosting/Hosting-1323038018006042547/original/836b4b69-dd4f-4ea7-a8ec-300754fe21e6.jpeg?im_w=1200",
            title="Gesamte Unterkunft: Privatunterkunft in Ostend, Belgien",
            location="Ostend, Belgien",
            beds=2,
            rooms=2,
            price_per_night=136,
            link="https://www.airbnb.de/rooms/1323038018006042547?search_mode=regular_search&adults=1&category_tag=Tag%3A8102&check_in=2025-07-01&check_out=2025-07-06&children=0&infants=0&pets=0&photo_id=2220940964&source_impression_id=p3_1751221983_P313shXL2kkaSRBe&previous_page_section_name=1000&federated_search_id=09b4df56-0cd6-4ae0-8106-85b46db748a5"
        ),
    ]
    
    db.session.bulk_save_objects(entries)
    db.session.commit()
    print(f"{len(entries)} Einträge wurden erfolgreich eingefügt!!!")
