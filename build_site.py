
def build():
    f = open("pub/index.html","w")
    f.write("""
            <html>
            <body>
                <h1>Hello World!</h1>
            </body>
            </html>
            """)
    f.close()

if __name__ == "__main__":
    build()
