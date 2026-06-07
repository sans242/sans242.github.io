# How to Manage Your Blog Posts

Since the design, layout, and styling are fully automated, you only ever need to write plain text to update your blog! Here is your quick reference guide:

## 1. How to Edit an Existing Post
1. Open the folder `D:\Antigravity\_posts` on your computer using a text editor (like VS Code, Notepad, or Obsidian).
2. Open the file you want to edit (e.g., `2026-06-07-gorakh-dhanda.md`).
3. Scroll past the `---` block at the top and just edit the text exactly like you would in a Word document.
4. Save the file.
5. Open your terminal in `D:\Antigravity` and push the changes to GitHub:
   ```bash
   git add .
   git commit -m "Updated post content"
   git push origin main
   ```
   *GitHub Pages will automatically rebuild and update the live site.*

## 2. How to Create a New Post
Whenever you want to write a new essay, just follow these steps:
1. Create a new `.md` file inside the `_posts` folder.
2. **Crucial:** You must name the file with the date first, like this: `2026-06-15-my-new-post.md`.
3. Open the file and copy-paste this block at the very top (this is called "Front Matter"):
   ```yaml
   ---
   layout: post
   title: "Your Title Here"
   subtitle: "An optional subtitle"
   date: 2026-06-15
   tags: [tech, thoughts]
   ---
   ```
4. Below the second `---`, just start typing your essay using standard Markdown. 
   - Use `**bold**` for bold text
   - Use `*italics*` for italics
   - Use `[Link text](URL)` for links
   - Use `## Heading` for section headers
5. Save, commit, and push! 

The website will automatically generate the beautiful layout, add the icons, calculate the reading time, and link it on your main Posts page. You only need to touch the code if you want to redesign the website itself!
