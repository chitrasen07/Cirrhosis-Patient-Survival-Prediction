# 🚀 **Step-by-Step Setup Guide**
## Cirrhosis Patient Survival Prediction Project

### 📋 **Table of Contents**
1. [Prerequisites](#prerequisites)
2. [Step 1: Clone Repository](#step-1-clone-repository)
3. [Step 2: Install Python](#step-2-install-python)
4. [Step 3: Create Virtual Environment](#step-3-create-virtual-environment)
5. [Step 4: Install Dependencies](#step-4-install-dependencies)
6. [Step 5: Run the Project](#step-5-run-the-project)
7. [Step 6: Verify Installation](#step-6-verify-installation)
8. [Troubleshooting](#troubleshooting)
9. [Development Workflow](#development-workflow)

---

## 🖥️ **Prerequisites**

Before starting, ensure you have:
- **Internet connection** for downloading packages
- **Git** installed on your system
- **Administrator/root access** (for some installations)
- **2GB free disk space**

---

## 📥 **Step 1: Clone Repository**

### **1.1 Open Terminal/Command Prompt**

**Windows:**
- Press `Win + R`, type `cmd`, press Enter
- Or press `Win + X`, select "Command Prompt" or "PowerShell"

**macOS:**
- Press `Cmd + Space`, type "Terminal", press Enter
- Or go to Applications → Utilities → Terminal

**Linux:**
- Press `Ctrl + Alt + T`
- Or search for "Terminal" in applications

### **1.2 Navigate to Your Desired Directory**

```bash
# Navigate to your Documents folder (or wherever you want the project)
cd Documents

# Or create a new folder for projects
mkdir Projects
cd Projects
```

### **1.3 Clone the Repository**

```bash
# Clone the repository
git clone https://github.com/yourusername/Cirrhosis-Patient-Survival-Prediction.git

# Navigate into the project directory
cd Cirrhosis-Patient-Survival-Prediction
```

**✅ Verification:** You should see the project files:
```
Cirrhosis-Patient-Survival-Prediction/
├── cirrhosis_survival_prediction.ipynb
├── requirements.txt
├── README.md
└── SETUP_GUIDE.md
```

---

## 🐍 **Step 2: Install Python**

### **2.1 Check if Python is Already Installed**

```bash
# Check Python version
python --version

# If Python is not found, try:
python3 --version
```

### **2.2 Install Python (if not installed)**

#### **Windows:**
1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.9 or 3.10
3. **Important:** Check "Add Python to PATH" during installation
4. Run the installer as administrator

#### **macOS:**
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### **2.3 Verify Python Installation**

```bash
# Check Python version (should be 3.8+)
python --version

# Check pip version
pip --version
```

**✅ Expected Output:**
```
Python 3.9.x
pip 21.x.x
```

---

## 🔧 **Step 3: Create Virtual Environment**

### **3.1 Navigate to Project Directory**

```bash
# Make sure you're in the project directory
cd Cirrhosis-Patient-Survival-Prediction

# List files to confirm
ls  # macOS/Linux
dir  # Windows
```

### **3.2 Create Virtual Environment**

```bash
# Create virtual environment
python -m venv .venv

# On some systems, you might need:
python3 -m venv .venv
```

### **3.3 Activate Virtual Environment**

#### **Windows:**
```bash
# Command Prompt
.venv\Scripts\activate

# PowerShell
.venv\Scripts\Activate.ps1
```

#### **macOS/Linux:**
```bash
source .venv/bin/activate
```

### **3.4 Verify Virtual Environment**

```bash
# You should see (.venv) in your prompt
# Windows: (.venv) C:\Users\...\Cirrhosis-Patient-Survival-Prediction>
# macOS/Linux: (.venv) user@computer:~/Cirrhosis-Patient-Survival-Prediction$

# Check Python location
where python  # Windows
which python  # macOS/Linux
```

**✅ Expected Output:**
```
# Windows
C:\Users\...\Cirrhosis-Patient-Survival-Prediction\.venv\Scripts\python.exe

# macOS/Linux
/home/user/Cirrhosis-Patient-Survival-Prediction/.venv/bin/python
```

---

## 📦 **Step 4: Install Dependencies**

### **4.1 Upgrade pip**

```bash
# Upgrade pip to latest version
python -m pip install --upgrade pip
```

### **4.2 Install Required Packages**

```bash
# Install all required packages
pip install -r requirements.txt
```

### **4.3 Verify Package Installation**

```bash
# Check if all packages are installed
pip list

# Test critical imports
python -c "import pandas, numpy, matplotlib, seaborn, sklearn, xgboost, joblib, jupyter; print('✅ All packages installed successfully!')"
```

**✅ Expected Output:**
```
✅ All packages installed successfully!
```

### **4.4 Install Jupyter Extensions (Optional)**

```bash
# Install Jupyter extensions for better experience
pip install jupyterlab
pip install ipywidgets
```

---

## 🚀 **Step 5: Run the Project**

### **5.1 Start Jupyter Notebook**

```bash
# Start Jupyter Notebook
jupyter notebook

# Alternative: Start Jupyter Lab
jupyter lab
```

### **5.2 Open the Project Notebook**

1. **Jupyter will open in your browser** (usually `http://localhost:8888`)
2. **Click on** `cirrhosis_survival_prediction.ipynb`
3. **Wait for the notebook to load**

### **5.3 Run the Notebook**

#### **Option A: Run All Cells (Recommended for first time)**
1. Click **"Cell"** in the menu bar
2. Select **"Run All"**
3. Wait for all cells to complete (this may take 5-10 minutes)

#### **Option B: Run Cells Sequentially**
1. Click on the first cell
2. Press **Shift + Enter** to run the cell
3. Wait for it to complete
4. Move to the next cell and repeat

### **5.4 What to Expect**

The notebook will:
1. **Load/Create sample data** (if `cirrhosis.csv` is missing)
2. **Preprocess the data** (handle missing values, encode categories)
3. **Perform exploratory data analysis** (create visualizations)
4. **Train multiple ML models** (Logistic Regression, Random Forest, XGBoost, SVM, KNN)
5. **Compare model performance** (show accuracy, precision, recall)
6. **Select the best model** and perform hyperparameter tuning
7. **Save the trained model** and scaler
8. **Create prediction function** for new data

### **5.5 Generated Files**

After successful execution, you should see these new files:
```
Cirrhosis-Patient-Survival-Prediction/
├── cirrhosis_survival_prediction.ipynb
├── cirrhosis.csv                    # Dataset (auto-generated if missing)
├── cirrhosis_model.pkl             # Trained model
├── cirrhosis_scaler.pkl            # Feature scaler
├── feature_names.pkl               # Feature names
├── requirements.txt
├── README.md
└── SETUP_GUIDE.md
```

---

## ✅ **Step 6: Verify Installation**

### **6.1 Check Generated Files**

```bash
# List all files in the project
ls  # macOS/Linux
dir  # Windows

# Verify model files exist
ls *.pkl  # macOS/Linux
dir *.pkl  # Windows
```

### **6.2 Test the Prediction Function**

1. **Scroll to the bottom** of the notebook
2. **Find the prediction demo cell**
3. **Run it** to test the trained model
4. **Verify the output** shows prediction results

### **6.3 Check Model Performance**

Look for these outputs in the notebook:
- **Model comparison table** with accuracy scores
- **Confusion matrix** visualization
- **Feature importance** chart
- **Performance metrics** (precision, recall, F1-score)

---

## 🛠️ **Troubleshooting**

### **Common Issues and Solutions**

#### **Issue 1: "python: command not found"**

**Solution:**
```bash
# Windows: Reinstall Python and check "Add to PATH"
# macOS: Install using Homebrew
brew install python

# Linux: Install Python
sudo apt install python3 python3-pip
```

#### **Issue 2: "pip: command not found"**

**Solution:**
```bash
# Install pip
python -m ensurepip --upgrade

# Or download get-pip.py and run:
python get-pip.py
```

#### **Issue 3: "Permission denied" errors**

**Solution:**
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows
```

#### **Issue 4: XGBoost installation fails**

**Solution:**
```bash
# Try installing without cache
pip install xgboost --no-cache-dir

# Or install from conda
conda install -c conda-forge xgboost
```

#### **Issue 5: Jupyter not starting**

**Solution:**
```bash
# Install Jupyter
pip install jupyter

# Try different port
jupyter notebook --port=8889

# Check if port is in use
netstat -an | grep 8888  # macOS/Linux
netstat -an | findstr 8888  # Windows
```

#### **Issue 6: Memory errors during training**

**Solution:**
- Close other applications
- Reduce batch size in the notebook
- Use smaller dataset for testing

#### **Issue 7: Dataset not found**

**Solution:**
- The notebook will create sample data automatically
- If you have your own dataset, place it in the project root
- Ensure the CSV file has the correct column names

### **Platform-Specific Issues**

#### **Windows PowerShell Issues:**
```bash
# If PowerShell execution policy blocks scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Use Command Prompt instead
cmd
.venv\Scripts\activate
```

#### **macOS M1 Chip Issues:**
```bash
# Install packages with specific flags
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt
```

#### **Linux Permission Issues:**
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-venv

# Use virtual environment to avoid permission issues
python3 -m venv .venv
source .venv/bin/activate
```

---

## 🔄 **Development Workflow**

### **For New Collaborators:**

#### **Step 1: Fork the Repository**
1. Go to the GitHub repository
2. Click "Fork" button
3. Clone your fork:
```bash
git clone https://github.com/yourusername/Cirrhosis-Patient-Survival-Prediction.git
```

#### **Step 2: Set Up Development Environment**
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Follow steps 1-6 above to set up environment
```

#### **Step 3: Make Changes**
1. Edit the notebook or create new files
2. Test your changes thoroughly
3. Ensure all cells run without errors

#### **Step 4: Commit and Push**
```bash
# Add your changes
git add .

# Commit with descriptive message
git commit -m "Add: Brief description of your changes"

# Push to your fork
git push origin feature/your-feature-name
```

#### **Step 5: Create Pull Request**
1. Go to GitHub
2. Click "New Pull Request"
3. Select your feature branch
4. Add description of changes
5. Request review from team members

### **For Existing Collaborators:**

#### **Step 1: Update Local Repository**
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade
```

#### **Step 2: Test Changes**
```bash
# Run the notebook to ensure everything works
jupyter notebook cirrhosis_survival_prediction.ipynb
```

---

## 📁 **Project Structure Explained**

```
Cirrhosis-Patient-Survival-Prediction/
├── 📓 cirrhosis_survival_prediction.ipynb    # Main Jupyter notebook
├── 📊 cirrhosis.csv                           # Dataset (418 patients, 17 features)
├── 🤖 cirrhosis_model.pkl                    # Trained ML model
├── ⚖️ cirrhosis_scaler.pkl                   # Feature scaling parameters
├── 📝 feature_names.pkl                      # Feature names for prediction
├── 📋 requirements.txt                       # Python package dependencies
├── 📖 README.md                             # Project overview and documentation
├── 🚀 SETUP_GUIDE.md                         # This step-by-step setup guide
├── 🎨 app.py                                # Streamlit web app (optional)
└── 📁 .venv/                                # Virtual environment (local only)
```

### **File Descriptions:**

- **`cirrhosis_survival_prediction.ipynb`**: Complete ML pipeline with data preprocessing, model training, and evaluation
- **`cirrhosis.csv`**: Mayo Clinic dataset with 418 patient records and 17 clinical features
- **`cirrhosis_model.pkl`**: Serialized trained model (Random Forest or XGBoost)
- **`cirrhosis_scaler.pkl`**: StandardScaler object for feature normalization
- **`feature_names.pkl`**: List of feature names for making predictions
- **`requirements.txt`**: List of required Python packages with specific versions
- **`app.py`**: Streamlit web application for interactive predictions (optional)

---

## 🎯 **Quick Start Checklist**

For new collaborators, follow this checklist:

- [ ] **Step 1**: Clone the repository
- [ ] **Step 2**: Install Python 3.8+
- [ ] **Step 3**: Create virtual environment
- [ ] **Step 4**: Activate virtual environment
- [ ] **Step 5**: Install dependencies from requirements.txt
- [ ] **Step 6**: Start Jupyter Notebook
- [ ] **Step 7**: Open cirrhosis_survival_prediction.ipynb
- [ ] **Step 8**: Run all cells in the notebook
- [ ] **Step 9**: Verify all generated files are created
- [ ] **Step 10**: Test the prediction function
- [ ] **Step 11**: Review the model performance results
- [ ] **Step 12**: Set up development environment
- [ ] **Step 13**: Create your first feature branch
- [ ] **Step 14**: Make a small test change
- [ ] **Step 15**: Submit your first pull request

---

## 📞 **Getting Help**

### **If You're Stuck:**

1. **Check the Documentation**
   - Read this setup guide thoroughly
   - Review the README.md file
   - Check inline comments in the notebook

2. **Common Resources**
   - [Jupyter Documentation](https://jupyter.org/documentation)
   - [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
   - [Pandas Documentation](https://pandas.pydata.org/docs/)
   - [XGBoost Documentation](https://xgboost.readthedocs.io/)

3. **Ask for Help**
   - Create an issue on GitHub
   - Tag relevant team members
   - Provide error messages and system information
   - Include your operating system and Python version

### **Contact Information:**

- **Project Maintainers**: 
  - Karunya Kalkhundiya
  - Chitrasen Singh
  - Ankit Mittal
  - Ratan Raj

- **GitHub Issues**: Use the Issues tab for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas

---

## 🎉 **Success Indicators**

You'll know the setup is successful when:

1. ✅ **Jupyter Notebook opens** without errors
2. ✅ **All notebook cells run** without errors
3. ✅ **Generated files are created** (cirrhosis_model.pkl, cirrhosis_scaler.pkl, feature_names.pkl)
4. ✅ **Model performance metrics** are displayed
5. ✅ **Prediction function works** and shows results
6. ✅ **Visualizations are generated** (heatmaps, charts, plots)

---

**🎉 Welcome to the Cirrhosis Patient Survival Prediction project!**

*This step-by-step guide should help you get started quickly. If you encounter any issues not covered here, please create an issue on GitHub or reach out to the team.*

---

## 📝 **Additional Notes**

### **Performance Tips:**
- The notebook may take 5-10 minutes to run completely
- Ensure you have at least 4GB RAM available
- Close other applications to free up memory
- The first run will be slower due to package compilation

### **Data Privacy:**
- The project uses the Mayo Clinic dataset (1974-1984)
- This is a historical dataset for research purposes
- Always consult healthcare professionals for medical decisions
- The model is for educational and research purposes only

### **Version Compatibility:**
- Python 3.8+ required
- All package versions are specified in requirements.txt
- Virtual environment ensures consistent package versions
- Tested on Windows 10/11, macOS 10.14+, and Ubuntu 18.04+
