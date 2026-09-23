# 🎓 Automatic Certificate Generator

A Python-based **Automatic Certificate Generator** that creates personalised certificates from a template and a CSV file containing participant names.

The program automatically adds each name to the certificate template and saves individual certificates in the output directory.

---

## 🎮 Features

- 🎓 Automatic certificate generation
- 📄 Reads names from a CSV file
- 🖼️ Uses a custom certificate template
- ✍️ Automatically places names on the certificate
- 🎯 Centres the recipient name horizontally
- 📁 Generates separate certificate files
- 🔄 Supports multiple names
- ⚡ Fast batch certificate generation
- 🐍 Simple Python-based implementation

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas**
- **Pillow (PIL)**

---

## 📂 Project Structure

```text
Automatic-Certificate-Generator/
│
├── main.py
├── list.csv
├── certificate.png
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RaavanHrishi07/Automatic-Certificate-Generator.git
```

### 2. Navigate to the Project

```bash
cd Automatic-Certificate-Generator
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Program

```bash
python main.py
```

The generated certificates will be saved inside the `pictures` folder.

---

## 📋 Input CSV

The `list.csv` file contains the names that will be printed on the certificates.

Example:

```csv
name
Achalesh Lakhotiya
John Doe
Jane Doe
```

Each row is processed individually by the program.

---

## 🖼️ Certificate Template

The project uses `certificate.png` as the certificate template.

The program opens the template and adds the recipient's name to it before saving the generated certificate.

---

## ⚙️ How It Works

1. The program reads the names from `list.csv`.
2. The certificate template is loaded.
3. A certificate is created for each name.
4. The recipient name is positioned in the centre of the certificate.
5. The completed certificate is saved as a PNG file.
6. The process continues until all names have been processed.

---

## 📁 Output

Generated certificates are saved inside:

```text
pictures/
```

Each certificate is saved using the recipient's name.

Example:

```text
pictures/
├── Achalesh Lakhotiya.png
├── John Doe.png
└── Jane Doe.png
```

---

## 🧪 Testing

The project was tested locally using:

```text
Python 3.11.9
Pandas
Pillow
```

The following components were tested:

- CSV file reading
- Certificate template loading
- Name generation
- Name positioning
- Multiple certificate generation
- PNG file output

---

## ⚠️ Important Notes

- `certificate.png` must be present in the project directory.
- `list.csv` must contain a `name` column.
- The `pictures` folder is created/used for generated certificates.
- Avoid using special characters in names that may not be valid in Windows filenames.
- Generated certificates are excluded from Git using `.gitignore`.

---

## 💡 Future Improvements

Possible future improvements include:

- 🖥️ Graphical User Interface (GUI)
- ✏️ Custom font selection
- 🎨 Multiple certificate templates
- 📅 Automatic date insertion
- 🏷️ Custom course/event title
- 📝 Custom certificate message
- 🖼️ Logo support
- 📊 Progress indicator
- 📦 ZIP download of all certificates
- 📄 PDF certificate generation
- 🔤 Automatic font-size adjustment for long names

---

## 🎯 Purpose

This project was created to practise and demonstrate:

- Python programming
- CSV data processing
- Pandas
- Pillow image processing
- Text rendering on images
- File handling
- Batch automation

---

## 👨‍💻 Author

**Hrishikesh Sharma**

GitHub: [RaavanHrishi07](https://github.com/RaavanHrishi07)

---

## 📄 License

This project is intended for educational and personal use.