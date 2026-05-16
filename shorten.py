import re

file_path = 'd:\\Web pages\\Softappix\\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Web Dev
html = re.sub(
    r'<p class="service-description">Specializing in React, Vite, and modern UI/UX to create lightning-fast, responsive websites that engage users and drive conversions\.</p>\s*<ul class="service-features">.*?</ul>',
    '<p class="service-description">Lightning-fast, responsive websites built with modern UI/UX to engage users and drive conversions.</p>',
    html, flags=re.DOTALL
)

# Digital Strategy
html = re.sub(
    r'<p class="service-description">Scaling businesses through targeted marketing and SEO\. We help you reach the right audience with the right message\.</p>\s*<ul class="service-features">.*?</ul>',
    '<p class="service-description">Data-driven SEO and targeted marketing to help you reach the right audience and scale your business.</p>',
    html, flags=re.DOTALL
)

# E-commerce
html = re.sub(
    r'<p class="service-description">Custom integrations for platforms like IndiaMart sellers\. Build your online store with seamless payment gateways\.</p>\s*<ul class="service-features">.*?</ul>',
    '<p class="service-description">Seamless online storefronts and payment integrations designed to convert visitors into loyal customers.</p>',
    html, flags=re.DOTALL
)

# AI
html = re.sub(
    r'<p class="service-description">Implementing intelligent features into existing workflows\. Automate processes and enhance user experience with AI\.</p>\s*<ul class="service-features">.*?</ul>',
    '<p class="service-description">Smart automation and intelligent chatbots that embed cutting-edge AI directly into your business workflows.</p>',
    html, flags=re.DOTALL
)

# Mobile
html = re.sub(
    r'<p class="service-description">Building cross-platform mobile applications that provide native-like experiences\. We turn your ideas into functional mobile products\.</p>\s*<ul class="service-features">.*?</ul>',
    '<p class="service-description">Powerful cross-platform mobile applications that deliver native-like performance and intuitive user experiences.</p>',
    html, flags=re.DOTALL
)

# Logo
html = re.sub(
    r'<p class="service-description">Crafting memorable and professional brand identities\. We design logos that capture your business essence and stand out\.</p>\s*<ul class="service-features">.*?</ul>',
    '<p class="service-description">Memorable brand identities and professional logos that capture your business essence and stand out in the market.</p>',
    html, flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
