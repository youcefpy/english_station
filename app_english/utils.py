

def lesson_upload_path(instance, filename):
    return f"lesson/{instance.stream.level}/{instance.stream.name}/{instance.unit.name}/{filename}"