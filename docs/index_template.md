# Dr. Westerbaan's Lecture Notes

Below are links to notes used at Lander University:

{% for class in classes %}
<!-- ## {{ class.get('name') }} -->

## [{{ class.get('file_name') }}](https://github.com/pwesterbaan/lander_lecture_notes/raw/main/{{ class.get('file_name') }})
<details>
  <summary>{{ class.get('name') }} Annotated Notes</summary>
    <ul> {{ class.get('notes_list') }} </ul>
</details>

{% endfor %}