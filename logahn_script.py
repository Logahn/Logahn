>>> from people import developers
>>> from skills import versatile, shiftless
>>> def developer_attributes(name):
        """
            Returns attributes for name
        """
        info = {}
        versatile_developers = versatile.good(developers.name)
        shiftless_developers = shiftless.bad(developers.name)

        #check versatile developers
        if name in versatile_developers:
            info.update(developers.skills.good[name])
   
        #check shifless developers
        if name in shiftless_developers:
            info.update(developers.skills.bad[name])
        return info
>>>
>>> Adele = developers('Adele', sorted(developer_attributes('Adele Chinda')))
>>>
>>> Adele.education
"Belgorod State University"
>>>
>>> Adele.major
"Applied Computer Science"
>>>
>>> Adele.degree
"Bachelors"
>>> Adele.interests
[
   "Artificial Intelligence", "Basketball", "AI Research", "Robotics programming", "Space Exploration"
]
>>>