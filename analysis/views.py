import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from django.shortcuts import render
from .forms import UploadFileForm  # Import the UploadFileForm class

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)
            summary = df.describe()
            head = df.head()

            # Generate a histogram
            plt.figure(figsize=(10, 6))
            # Handle case where there are no numerical columns
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
            if not numeric_cols.empty:
                sns.histplot(df[numeric_cols[0]], kde=True)
                plt.title('Histogram of ' + numeric_cols[0])
            else:
                plt.text(0.5, 0.5, 'No numerical columns to plot', horizontalalignment='center', verticalalignment='center')
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')

            context = {
                'form': form,
                'summary': summary.to_html(),
                'head': head.to_html(),
                'image': image_base64,
            }
            return render(request, 'analysis/result.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
