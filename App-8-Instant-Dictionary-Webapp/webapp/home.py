import justpy as jp


class Home:
    path = '/'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        This is some text, testing text. lkasdlsfkdn s
        fjdskodiflkwemf lkdsjflsdiuwelk lksjdf weilkl
         sdfljeif sld ljsfjlj slj nsnlfjl""", classes="text-lg")
        return wp