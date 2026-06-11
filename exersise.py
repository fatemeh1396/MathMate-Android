import flet as ft

def main(page: ft.Page):
    page.title = "ابزارهای فلت"
    page.window_width = 400
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.DARK

    # ۱. فیلد نوشتن
    input_field = ft.TextField(label="اسم خودت رو بنویس")

    # ۲. منوی کرکره‌ای
    dropdown_menu = ft.Dropdown(
        label="زبان مورد علاقه",
        options=[
            ft.dropdown.Option("پایتون (Python)"),
            ft.dropdown.Option("جاوا اسکریپت (JS)"),
            ft.dropdown.Option("سی شارپ (#C)"),
        ]
    )

    # ۳. دکمه
    def button_clicked(e):
        result_text.value = f"سلام {input_field.value}! تو عاشق {dropdown_menu.value} هستی!"
        page.update()

    # در فلت جدید: ElevatedButton تبدیل به Button شده و text تبدیل به content شده است!
    my_button = ft.Button(
        content=ft.Text("ثبت اطلاعات"), 
        on_click=button_clicked
    )

    # متن خالی برای نتیجه
    result_text = ft.Text(value="", size=16, color="green")

    # اضافه کردن به صفحه
    page.add(
        input_field,
        dropdown_menu,
        my_button,
        result_text
    )


ft.run(main)