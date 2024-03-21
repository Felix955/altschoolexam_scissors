# from sqlalchemy.orm import Session
# from models import URL

# def create_shortened_url(db: Session, old_url: str) -> URL:
#     new_url = generate_new_url() # Implement this function to generate new URL
#     db_url = URL(old_url=old_url, new_url=new_url)
#     db.add(db_url)
#     db.commit()
#     db.refresh(db_url)
#     return db_url



from sqlalchemy.orm import Session
import shortuuid
from models import ShortenedURL


def create_shortened_url(db: Session, long_url: str) -> ShortenedURL:
    new_id = shortuuid.uuid()
    shortened_url = ShortenedURL(id=new_id, old_url=long_url, new_url=f"http://example.com/{new_id}")
    db.add(shortened_url)
    db.commit()
    db.refresh(shortened_url)
    return shortened_url

def get_original_url(db: Session, shortened_url: str) -> str:
    url = db.query(ShortenedURL).filter(ShortenedURL.id == shortened_url).first()
    if url:
        return url.old_url
    return ""





