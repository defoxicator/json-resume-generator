# JSON CV Builder

def main():
    import json

    # data dictionaries  
    
    basics_dict = {
        "name": "Full name: ",
        "label": "Desired position: ",
        "image": "URL to your picture: ",
        "email": "E-mail address: ",
        "phone": "Phone number: ",
        "url": "URL to your website: ",
        "summary": "Description: ",
    }
    
    location_dict = {
        "address": "Address: ",
        "postalCode": "Postal code: ",
        "city": "City: ",
        "countryCode": "Country: ",
        "region": "Region: "
    }
 
    profiles_dict = {
        "network": "Social network: ",
        "username": "Username: ",
        "url": "URL: "
    } 

    work_dict = {
        "company": "Company: ",
        "url": "Company's website: ",
        "position": "Position: ",
        "startDate": "Start: ",
        "endDate": "End: ",
        "summary": "Description: ",
        "highlights": "Highlights: "
    }

    education_dict = {
        "institution": "Institution: ",
        "url": "institution's website: ",
        "area": "Subject: ",
        "studyType": "Study type: ",
        "startDate": "Start: ",
        "endDate": "End: ",
        "score": "GPA: ",
        "courses": "Relevant courses: ",
    }

    skills_dict = {
        "name": "Category/Name: ",
        "level": "Level: ",
        "keywords": "Keywords: "
    }

    languages_dict = {
        "language": "Language: ",
        "fluency": "Fluency: "
    }

    interests_dict = {
        "name": "Name: ",
        "keywords": "Keywords: "
    }
    
    projects_dict = {
      "name": "Name: ",
      "description": "Description: ",
      "highlights": "Highlights: ",
      "keywords": "Keywords: ",
      "entity": "Entity: ",
      "type": "Type of project: "
    }
    
    high_keyw_list = ["highlights", "keywords", "courses"]

    resume = {}
    basics = {}

    def more_entries(category):
        agree = input(f"Do you have anything to add to {category}? (y/n) ")

        if agree.lower() in ["y", "yes"]:
            return True
        else:
            return False

    def listed_content(name):
        list_cont = []

        if more_entries(name) == True:
            list_cont.append(str(input(f'Input one of your {name}: ')))
        
            while more_entries(name) == True:
                list_cont.append(str(input(f'Input one of your {name}: ')))

        return list_cont
    
    def single_section(list, names):
        template_copy = template.copy()

        for k, v in template_copy.items():
            if k not in high_keyw_list:
                template_copy[k] = str(input(template[k]))
            else:
                continue
        
        if names:
            for name in names:
                template_copy.update({name: listed_content(name)})
            
            
        list.append(template_copy)

    def section(category, names = None):
        if more_entries(category) == True:
            list = []
            single_section(list, names)
            
            while more_entries(category) == True:
                single_section(list, names)

            if category == "profiles":
                basics.update({"profiles": list})
                resume.update({"basics": basics})
            else:
                resume.update({category: list})

    def save():
        saved = 0
        while saved == 0:
            if str(input("Do you want to save your resume? (y/n)")).lower() in ["y", "yes"]:

                format = str(input("In which format? (txt/json) ")).lower()
                if format in ["txt", ".txt", "text"]:
                    with open('resume.txt', 'w') as f:
                        f.write(str(resume))
                        saved = 1

                elif format in ["json", ".json"]:
                    with open('resume.json', 'w') as f:
                        json_object = json.dumps(resume, indent = 2) 
                        f.write(json_object)
                        saved = 1

                else:
                    print("Wrong format")
            
            else:
                saved = 1


    print("""
    Welcome to CV Builder. Let's build that JSON!
    """)

    templates = [basics_dict, location_dict, profiles_dict, work_dict, education_dict, skills_dict, languages_dict, interests_dict, projects_dict]
    
    templates_dict = {
        "basics": (basics_dict, []),
        "location": (location_dict, []),
        "profiles": (profiles_dict, []),
        "work": (work_dict, ["highlights"]),
        "education": (education_dict, ["courses"]),
        "skills": (skills_dict, ["keywords"]),
        "languages": (languages_dict, []),
        "interests": (interests_dict, ["keywords"]),
        "projects": (projects_dict, ["highlights", "keywords"])      
    }

    if str(input("Do you want to include theme https://jsonresume.org/ theme? (y/n)")).lower() in ["y", "yes"]:
        theme_dict = {"meta": {"theme": str(input("Theme: "))}}
        resume.update(theme_dict)

    for k, v in templates_dict.items():
        template = v[0]

        if k == "basics":
            template_copy = template.copy()

            for k, v in template_copy.items():
                template_copy[k] = str(input(template[k]))
                basics.update(template_copy)

        elif k == "location":
            template_copy = template.copy()

            for k, v in template_copy.items():
                template_copy[k] = str(input(template[k]))
                basics.update({"location": template_copy})

        else:
            section(k, v[1])
    
    save()
    
if __name__ == "__main__":
    main()