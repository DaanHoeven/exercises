# Write your code here
import re

string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random HTML Document</title>
</head>
<body>
    <h1>Welcome to my Random HTML Document</h1>
    
    <p>Here is some random text:</p>
    
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed <a href="https://example.com">link</a> dapibus, neque ut cursus elementum, velit ipsum pretium nisi, at finibus purus ante eu justo. Nunc ultrices vehicula ultrices. Vestibulum malesuada turpis at arcu malesuada, vel dictum orci feugiat. Vestibulum lacinia dapibus nulla, vel suscipit nulla lobortis et. Nulla auctor sodales sapien, in sagittis felis scelerisque nec. Nullam in libero a lorem sollicitudin elementum.</p>
    
    <p>Phasellus vitae velit <a href="https://Bol.com">link</a> vitae magna placerat eleifend. Nulla facilisi. Nullam maximus fringilla lacus. Proin at dapibus arcu. Etiam vel odio vitae sem consectetur facilisis. Duis vel convallis ligula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nulla tempus est vitae metus efficitur, et fermentum elit pharetra.</p>
    
    <p>Donec nec turpis ac odio aliquam volutpat a eu orci. Sed commodo magna vitae metus lobortis, at semper eros porttitor. Aenean aliquet malesuada turpis eget eleifend. Fusce sed turpis eget est lobortis rhoncus nec vel enim. Duis condimentum nulla a orci vestibulum, vitae faucibus orci mattis. Phasellus eu dolor nec nisi gravida tincidunt vel id nisl.</p>
    
    <p>Thank you for visiting!</p>

    <h2>More Links</h2>

    <ul>
        <li><a href="https://www.example1.com">Example 1</a></li>
        <li><a href="https://www.example2.com">Example 2</a></li>
        <li><a href="https://www.example3.com">Example 3</a></li>
    </ul>
</body>
</html>
"""


def collect_links(string):
    return re.findall(r'<a href="(.*)">', string)


print(collect_links(string))
