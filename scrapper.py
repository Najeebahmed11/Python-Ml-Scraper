from recipe_scrapers import scrape_me
import time
st = time.time()
scraper = scrape_me('https://www.closetcooking.com/sweet-potato-gratin/', wild_mode=True)
# if no error is raised - there's schema available:
scraper.title()
scraper.instructions()  # etc

print("Name Result: " + scraper.title())
print("\n")
print("Ingredient Result: " )
print(scraper.ingredients())
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')