import argparse
from urllib.parse import urljoin
from hashlib import sha1

def compute_hash(email):
    return sha1(email.encode('utf-8')).hexdigest()

def compute_certificate_id(email):
    email_clean = email.lower().strip()
    return compute_hash(email_clean + '_')

def main(args):
    print(args)
    cohort = args.year
    course = args.course
    your_id = compute_certificate_id(args.email)
    url = urljoin(
        "https://certificate.datatalks.club", 
        "/".join([course, str(cohort), f"{your_id}.pdf"]))
    print(url)
    

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Generate a certificate for MLZoomCamp")
    argparser.add_argument("email", type=str, help="The email address of the recipient")
    argparser.add_argument("--year", type=int, help="The year for which to generate the certificate", default=2023)
    argparser.add_argument("--course", type=str, help="The course name", default="ml-zoomcamp")
    args = argparser.parse_args()
    main(args)