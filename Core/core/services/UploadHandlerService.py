def handle_uploaded_file(f):
    with open('./uploads/fileuploaded' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
