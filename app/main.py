from flask import Flask, render_template, request, redirect, url_for, flash
from utils.scraper import scrape_website_content

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # This is for flashing messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        description = request.form.get('description')

        # If a URL is provided, attempt to scrape
        if url:
            scraped_content = scrape_website_content(url)
            if scraped_content:
                # TODO: Use GPT-3 to get a concise description and then classify
                flash(f'Scraped content: {scraped_content[:100]}...',
                      'info')  # Displaying only first 100 chars as an example
                return redirect(url_for('index'))

            else:
                flash('Failed to scrape the provided URL. Please provide a description.', 'error')
                return redirect(url_for('index'))

        # If a description is provided, classify it directly
        elif description:
            # TODO: Classify the description
            flash('Description received. Classification will be implemented next.', 'info')
            return redirect(url_for('index'))
    return render_template('classification_form.html')


def classify_company(url=None, description=None):
    if url:
        # Add logic to scrape the website and classify based on the content
        pass  # For now, just a placeholder
    elif description:
        # Add logic to classify based on the description
        pass  # For now, just a placeholder
    else:
        return None

    # Return the classification result (for now just a placeholder)
    return "Sample Sector: Sample Sub-sector"

if __name__ == "__main__":
    app.run(debug=True)