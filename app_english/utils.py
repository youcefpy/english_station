

def lesson_upload_path(instance, filename):
    return f"lesson/{instance.stream.name}/{instance.unit.name}/{filename}"