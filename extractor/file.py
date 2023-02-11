def save_to_file(file_name, jobs):
    csv_file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")
    csv_file.write("company, title, location, link\n")
    for job in jobs:
        csv_file.write(
            f"{job['company']},{job['title']},{job['location']},{job['link']}\n")
    csv_file.close()
