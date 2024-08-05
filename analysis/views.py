import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

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
            sns.histplot(df.select_dtypes(include=['float64', 'int64']).columns[0], data=df, kde=True)
            plt.title('Histogram')
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
