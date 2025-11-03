# 🚀 Quick Run Instructions

## ✅ **The Issue Has Been Fixed!**

The encoding issue has been resolved. The notebook now includes a fix for Windows console encoding problems.

## 🎯 **How to Run the Project**

### **Method 1: Using Jupyter Notebook (Recommended)**

1. **Open Terminal/Command Prompt** and navigate to the project:
   ```bash
   cd "C:\Users\Chitraen singh\Documents\GitHub\Cirrhosis-Patient-Survival-Prediction"
   ```

2. **Activate Virtual Environment**:
   ```bash
   .venv\Scripts\Activate.ps1
   # Or if that doesn't work:
   .venv\Scripts\activate.bat
   ```

3. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

4. **Open the notebook** `cirrhosis_survival_prediction.ipynb` in your browser

5. **Run all cells**: Click "Cell" → "Run All"

### **Method 2: Execute from Command Line**

```bash
# Set encoding (Windows)
$env:PYTHONIOENCODING="utf-8"

# Run the notebook
.venv\Scripts\jupyter-nbconvert.exe --execute --to notebook --inplace cirrhosis_survival_prediction.ipynb
```

### **Method 3: Using Python Directly**

```bash
# Set encoding environment variable
$env:PYTHONIOENCODING="utf-8"

# Run Python
.venv\Scripts\python.exe

# Then import and run notebook cells manually
```

## 🛠️ **If You Still Get Errors**

### **Error: UnicodeEncodeError**

If you see encoding errors, run this command first:
```bash
$env:PYTHONIOENCODING="utf-8"
```

Or add this to your PowerShell profile:
```powershell
$env:PYTHONIOENCODING="utf-8"
```

### **Error: Module Not Found**

Install dependencies:
```bash
.venv\Scripts\pip.exe install -r requirements.txt
```

### **Error: Jupyter Not Found**

Install Jupyter:
```bash
.venv\Scripts\pip.exe install jupyter notebook
```

### **Error: Port Already in Use**

Use a different port:
```bash
jupyter notebook --port=8889
```

## 📋 **Expected Output**

After successful execution, you should have:

1. ✅ All cells executed without errors
2. ✅ Generated files:
   - `cirrhosis_model.pkl`
   - `cirrhosis_scaler.pkl`
   - `feature_names.pkl`
3. ✅ Model performance metrics displayed
4. ✅ Visualizations (heatmaps, charts, plots)
5. ✅ Prediction function ready to use

## 🎉 **Success Indicators**

- No red error messages in cells
- All cells show execution numbers (e.g., [1], [2], [3])
- Model files are generated
- Performance metrics are displayed
- Visualizations appear in the notebook

## 💡 **Tips**

1. **First Time Running**: Use "Run All" to execute everything sequentially
2. **If Cells Fail**: Run cells one by one to identify the problem cell
3. **Memory Issues**: Close other applications if you get memory errors
4. **Slow Execution**: The notebook may take 5-10 minutes to complete

## 📞 **Still Having Issues?**

1. Check that all packages are installed:
   ```bash
   .venv\Scripts\python.exe test_notebook.py
   ```

2. Verify the dataset exists:
   ```bash
   dir cirrhosis.csv
   ```

3. Check Python version:
   ```bash
   .venv\Scripts\python.exe --version
   # Should be 3.8 or higher
   ```

---

**Note**: The encoding fix has been automatically added to the notebook. If you still encounter issues, please share the exact error message.

