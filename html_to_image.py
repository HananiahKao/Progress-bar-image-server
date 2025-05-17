from playwright.sync_api import sync_playwright

def html_to_png(percentage, darkmode, output_file="progress.png"):
    if darkmode:
        color_scheme = "dark"
    else:
        color_scheme = "light"
    html_content = f"""
    <html>
        <head>
            <meta name="color-scheme" content="{color_scheme}">
        </head>
        <body>
            <div style="display: flex;
            align-items: center;
            width: 100%;
            background: #e0e0e0;
            border-radius: 12px;
            overflow: hidden;
            font-family: monospace;
            height: 24px;
            ">
                <div style="background: #4caf50;
                width: {percentage}%;
                height: 100%;
                "></div>
                <div style="margin-left: auto;
                padding: 0 8px;
                color: #333;
                ">{percentage}%</div>
            </div>
        </body>
    </html>
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1024, "height": 50})
        page.set_content(html_content)
        # Wait for all to load
        page.wait_for_timeout(500)
        # Take screenshot of the page content (clip to element if needed)
        page.screenshot(path=output_file, full_page=False)
        browser.close()
