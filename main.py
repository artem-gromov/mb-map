import folium
import streamlit as st
from folium.plugins import MarkerCluster

from streamlit_folium import st_folium

class Person:
    def __init__(self, name, job, desc, location, lat, lon):
        self.name = name
        self.job = job
        self.desc = desc
        self.location = location
        self.lat = lat
        self.lon = lon

    def popup(self):
        return f"""
        <div>
            <h4>{self.name}, {self.job}</h4>
            <p>{self.desc}</p>
        </div>
        """
    
persons = [
    Person(
        "Юлия", 
        "QA", 
        "Лечу решать баги. К своим хобби отношу лего любых форм и размеров и еще люблю играть в настолки или настойки (смотря в какой компании нахожусь)",
        "Грузии, Тбилиси",
        41.7151,44.8271
        ),
    Person(
        "Юлия",
        "QA",
        "Люблю заниматься рукоделием, вышивкой, судоку, Лего, присоединяюсь к Юле и настойкам!",
        "Казахстан, Астана",
        51.1605,71.4704
        ),
    Person(
        "Сэм",
        "TeamLead QA",
        "Люблю поесть и GAYming",
        "Кыргызстан, Бишкек",
        42.8746,74.5698
        ),
    Person(
        "Елена",
        "QA",
        "Люблю заниматься цветами, вышивкой, судоку и иногда спортзал",
        "Россия, Гусь-Хрустальный",
        56.0000,38.0000
        ),
    Person(
        "Анна",
        "QA",
        "Из увлечений: йога, книжки, архитектура",
        "Грузия, Тбилиси",
        41.7151, 44.8271
    ),
     Person(
        "Артур",
        "QA",
        "Главный факт обо мне: Продам родину за американский бургер",
        "Кыргызстан, Бишкек",
        42.8746, 74.5698
    ),
    Person(
        "Акылбек",
        "TeamLead QA",
        "Увлечения: футбол (болею за Арсенал, COYG), баскетбол (начал смотреть в этом году), компьютерные игры (сейчас играю только в шутер The Finals)",
        "Кыргызстан, Бишкек",
        42.8746, 74.5698
    ),
    Person(
        "Алихан",
        "QA",
        "Люблю спорт, и тренировать людей💪🏻",
        "Казахстан, Астана",
        51.1605, 71.4704
    ),
    Person(
        "Анжелика",
        "QA",
        "Из увлечений: Люблю вкусно поесть, поорать в караоке, домашний Йога-Фит)",
        "Кыргызстан, Бишкек",
        42.8746, 74.5698
    ),
    Person(
        "Виктор",
        "QA",
        "Интересы: 1. Убирать мусор в лесу, 2. Играть в настолки, 3. Читать фентези (читаю 2 года «Колесо времени»), 4. Смотреть формулу-1, 5. Думать как автоматизировать рутинные задачи",
        "Кыргызстан, Бишкек",
        42.8746, 74.5698
    ),
    Person(
        "Сергей",
        "QA",
        "Люблю спорт во всех его проявлениях, а также путешествовать)",
        "Польша, Катовице",
        50.0647, 19.9450
    ),
    Person(
        "Мадина",
        "QA",
        "Увлечения: Лыжи, хайкинг, прогулки с собакой",
        "Сербия, Нови-Сад",
        45.2671, 19.8335
    ),
    Person(
        "Андрей",
        "TeamLead QA",
        "Интересы / хобби: игры (преимущественно олдскульный синглплеер), еда, походы в бар, артхаусное и жанровое кино, сериалы, кулинарные шоу, технологии, альтернативная рок-музыка 80-х, 90-х и 2000-х, котики.",
        "Грузии, Тбилиси",
        41.7151, 44.8271
    ),
    Person(
        "Валентина",
        "QA",
        "Из увлечений: люблю пилонный спорт и путешествия",
        "Казахстан, Караганда",
        49.8000, 73.1000
    ),
    Person(
        "Салават",
        "Data Engineer",
        "Люблю фотографировать, тренировки и кока-колу",
        "Татарстан, Казань",
        55.8304, 49.0661
    ),
    Person(
        "Артем",
        "Data Engineer",
        "Люблю путешествовать, играть в компьютерные игры и смотреть сериалы",
        "Казахстан, Алматы",
        43.2220, 76.8512
    ),
    Person(
        "Сергей",
        "Information Security Specialist",
        "Люблю почитать книжку интересную, теннис, серфинг, пострелять в тире",
        "Россия, Москва",
        55.7558, 37.6173
    ),
    Person(
        "Михаил",
        "Data Engineer",
        "Люблю: пиво, не люблю: инциденты, лоббирую продвижение задач за фриспины",
        "Россия, Москва",
        55.7558, 37.6173
    ),
    Person(
        "Александр",
        "Data Engineer",
        "Люблю: путешествовать, не люблю: сидеть на месте",
        "Россия, Санкт-Петербург",
        59.9343, 30.3351
    ),
    Person(
        "Володя",
        "Data Engineer",
        "Главный по табличкам. Люблю: поспать, не люблю: просыпаться ночью из-за инцидентов",
        "Cyprus, Moniatis",
        34.6770, 33.0492
    ),
    Person(
        "Роман",
        "Data Engineer",
        "В свободное время музицирую на студии, занимаюсь гимнастикой, волейболом, изучаю и тестирую нейросети, веду тематический канал.  Могу поиграть в компьютерные игры, если прям сильно много свободного времени, что редкость, особенно в последний год.",
        "Сербия, Белград",
        44.7866, 20.4489
    ),
    Person(
        "Денис",
        "Data Architect",
        "Люблю экстремальные виды спорта, панк-рок, стоицизм, построение интеллектуальных систем",
        "Кипр, Лимассол",
        34.6770, 33.0492
    ),
    Person(
        "Артемий",
        "Head of Ratings",
        "Увлекаюсь современными технологиями, компьютерными играми, музыкой и туризмом.",
        "Россия, Иркутск",
        52.2860, 104.2806
    ),
    Person(
        "Александр",
        "Team Lead Ratings Team",
        "Интересы / хобби: футбол, горные лыжи, походы и путешествия, политика, загородный отдых, русский и иностранный рок",
        "Россия, Зеленоград",
        55.9833, 37.1833
    ),
    Person(
        "Екатерина",
        "Senior Reputation Manager",
        "Одесситка с тягой к теплым краям и терапевтическим морям. Читаю: от современной прозы до Гарри Поттера. Люблю квизы, но не люблю квесты. Адепт морских и не только прогулок.",
        "Бяла, Болгария",
        42.7833, 27.8333
    ),
    Person(
        "Илья",
        "Middle Reputation Manager",
        "Люблю быстрые машины, прогулки с собакой и дальние путешествия. Из активного спорта выбираю каякинг. Родом с южных берегов Крыма.",
        "Санкт-Петербург, Россия",
        59.9343, 30.3351
    )
]

st.set_page_config(
    page_title="Team Map",
    page_icon="🌍",
    layout="wide",
)
st.title("Adviva Team Map 🌍")

m = folium.Map(
    location=[34.6770, 33.0492], 
    zoom_start=3,
    tiles="OpenStreetMap",
)
marker_cluster = MarkerCluster().add_to(m)
for person in persons:
    folium.Marker(
        location=[person.lat, person.lon],
        popup=folium.Popup(person.popup(), max_width=300),
        icon=folium.Icon(),
    ).add_to(marker_cluster)

st_folium(m,  height=500, use_container_width=True)

st.dataframe(
    [
        {
            "Name": person.name,
            "Job": person.job,
            "Description": person.desc,
            "Location": person.location
        } for person in persons
    ]
)


# m.save("index.html")