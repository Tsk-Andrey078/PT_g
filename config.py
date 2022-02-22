host = "localhost"
port = 3306
user = "root"
password = "104212327501"
database = "mydb"

resource_list = (
    {
        "RESOURCE_NAME": "tengrinews",
        "RESOURCE_URL": "https://tengrinews.kz/find-out/",
        "top_tag": "div::class::tn-article-grid/div::class::tn-article-item",
        "bottom_tag": "",
        "title_cut": "span::class::tn-article-title",
        "date_cut": "time::none::none"
    },
    {
        "RESOURCE_NAME": "scientificrussia",
        "RESOURCE_URL": "https://scientificrussia.ru/news",
        "top_tag": "div::class::wrapper/div::class::announce/div::class::title",
        "bottom_tag": "div::class::announce/div::class::lead/p::none::none",
        "title_cut": "div::class::wrapper/div::class::announce/div::class::title/a::none::none",
        "date_cut": "time::none::none"
    }
)
     