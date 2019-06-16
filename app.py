from flask import Flask, render_template, request
from scraper import show_scraper
import download_manager

app = Flask(__name__)
domain = 'https://horriblesubs.info'
shows = show_scraper.scrap_shows_url(domain)
shows_map = {show.name: show for show in shows}
selected_show = shows[0]


@app.route('/', methods=['GET', 'POST'])
def render():
    new_selected_show = request.form.get('show')

    if new_selected_show:
        global selected_show
        selected_show = shows_map[request.form.get('show')]

    res = request.form.get('resolution')
    output_dir = request.form.get('output-directory')

    if res and res.isdigit() and output_dir:
        without_error, message = download_manager.download_show('magnet', selected_show.url,
                                                                int(res), output_dir, selected_show.name)
        if not without_error:
            # should render another html file with error
            print(message)

    # first time loading the show, have to scrap img and description
    if not selected_show.img:
        show_scraper.scrap_show_img_desc(selected_show, domain)

    return render_template('show.html', shows=shows, selected=selected_show)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
