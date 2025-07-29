import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-data'

mcp = FastMCP('fresh-linkedin-profile-data')

@mcp.tool()
def get_personal_profile(linkedin_url: Annotated[str, Field(description='')],
                         include_skills: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_certifications: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_publications: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_honors: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_volunteers: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_projects: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_patents: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_courses: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_organizations: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_profile_status: Annotated[Literal['false', 'true', None], Field(description='Enabling this option will cost an additional 0.5 credits.')] = None,
                         include_company_public_url: Annotated[Literal['false', 'true', None], Field(description='This option is free of charge.')] = None) -> dict: 
    '''Get comprehensive profile data, including experience, education history, and current company details. 1 credit per call. Using each extra option will cost another 0.5 credits.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
        'include_skills': include_skills,
        'include_certifications': include_certifications,
        'include_publications': include_publications,
        'include_honors': include_honors,
        'include_volunteers': include_volunteers,
        'include_projects': include_projects,
        'include_patents': include_patents,
        'include_courses': include_courses,
        'include_organizations': include_organizations,
        'include_profile_status': include_profile_status,
        'include_company_public_url': include_company_public_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def detect_activity_time(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get the time of the latest profile activity. 2 credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-recent-activity-time'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_profile_by_sales_nav_url(linkedin_url: Annotated[str, Field(description='')],
                                 include_skills: Annotated[Union[str, None], Field(description='')] = None,
                                 include_certifications: Annotated[Union[str, None], Field(description='')] = None,
                                 include_publications: Annotated[Union[str, None], Field(description='')] = None,
                                 include_honors: Annotated[Union[str, None], Field(description='')] = None,
                                 include_volunteers: Annotated[Union[str, None], Field(description='')] = None,
                                 include_projects: Annotated[Union[str, None], Field(description='')] = None,
                                 include_patents: Annotated[Union[str, None], Field(description='')] = None,
                                 include_courses: Annotated[Union[str, None], Field(description='')] = None,
                                 include_organizations: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get full profile data, including experience & education history, skillset and company related details. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile-by-salesnavurl'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
        'include_skills': include_skills,
        'include_certifications': include_certifications,
        'include_publications': include_publications,
        'include_honors': include_honors,
        'include_volunteers': include_volunteers,
        'include_projects': include_projects,
        'include_patents': include_patents,
        'include_courses': include_courses,
        'include_organizations': include_organizations,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def google_full_profiles(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Discover LinkedIn profiles via Google using details like job title, company, location, or keywords, and perform a comprehensive analysis to generate match scores. This endpoint is optimized to pinpoint LinkedIn contacts with precision, based on the basic information provided. Credit Cost: Base cost: 2 credits Additional cost: 1 credit per selected profile For example: Selecting 1 profile = 3 credits Selecting 2 profiles = 4 credits'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/google-full-profiles'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_profile_latest_post_date(linkedin_url: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Find out when he/she posted recently.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/profile-latest-post-date'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_company_by_url(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Retrieve valuable data points using a company’s LinkedIn URL. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-linkedinurl'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_company_by_domain(domain: Annotated[str, Field(description='')]) -> dict: 
    '''Find a company on LinkedIn using its web domain. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-domain'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_company_by_id(company_id: Annotated[str, Field(description='')]) -> dict: 
    '''Retrieve valuable data points using a company’s LinkedIn internal ID. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-id'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'company_id': company_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_company_insights(company_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get company insights from Linkedin sales navigator. 5 credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-insights'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'company_id': company_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def find_custom_headcount(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Discover the count of employees within a specific company who meet designated criteria. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/find-custom-headcount'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def count_job_openings(company_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get the number of job openings a company has posted on LinkedIn. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-jobs-count'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'company_id': company_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_profile_sposts(linkedin_url: Annotated[str, Field(description='')],
                       type: Annotated[Literal['posts', 'comments', 'reactions', None], Field(description='Possible values: posts: to scrape posts from tab Posts -- posts or posts reshared by the person comments: to scrape posts from tab Comments -- posts the person commented reactions: to scrape posts from tab Reactions -- posts the person reacted')] = None,
                       start: Annotated[Union[int, float, None], Field(description='Use this param to fetch posts of the next result page: 0 for page 1, 50 for page 2, etc. Default: 0')] = None,
                       pagination_token: Annotated[Union[str, None], Field(description='Required when fetching the next result page. Please use the token from the result of your previous call.')] = None) -> dict: 
    '''Retrieve posts from a person's profile. Pagination is supported for accessing all posts. 2 credits per call'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-posts'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
        'type': type,
        'start': start,
        'pagination_token': pagination_token,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_post_scomments(urn: Annotated[str, Field(description='')],
                       sort_by: Annotated[Union[str, None], Field(description='Default value: Most relevant. Possible values: Most relevant, Most recent.')] = None,
                       page: Annotated[Union[str, None], Field(description='')] = None,
                       pagination_token: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get comments of a post. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-post-comments'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'urn': urn,
        'sort_by': sort_by,
        'page': page,
        'pagination_token': pagination_token,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_post_sreactions(urn: Annotated[str, Field(description='')],
                        type: Annotated[Literal['ALL', 'LIKE', 'EMPATHY', 'APPRECIATION', 'INTEREST', 'PRAISE', None], Field(description='Default value: ALL. Possible values: ALL,LIKE,EMPATHY,APPRECIATION,INTEREST,PRAISE.')] = None,
                        page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get reactions of a post. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-post-reactions'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'urn': urn,
        'type': type,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_posts(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Simulates LinkedIn's Post Search Function with most important filters. 2 credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-posts'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_company_sposts(linkedin_url: Annotated[str, Field(description='')],
                       start: Annotated[Union[int, float, None], Field(description='Use this param to fetch posts of the next result page: 0 for page 1, 50 for page 2, etc. Default: 0')] = None,
                       pagination_token: Annotated[Union[str, None], Field(description='Required when fetching the next result page. Please use the token from the result of your previous call.')] = None,
                       sort_by: Annotated[Union[str, None], Field(description='Possible values: top, recent')] = None) -> dict: 
    '''Get posts from a LinkedIn company page. Pagination is supported to fetch all posts. 2 credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-posts'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
        'start': start,
        'pagination_token': pagination_token,
        'sort_by': sort_by,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_post_details(urn: Annotated[str, Field(description='')]) -> dict: 
    '''Scrape details of a single post based on its URN.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-post-details'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'urn': urn,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_employees(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Streamline your Sales Navigator lead searches effortlessly without connecting your own account. How the Process Works: Step 1: Initiate Search Launch your search with specific criteria via a dedicated endpoint. Upon request, you'll receive a unique "request_id" enabling continuous status checks in Step 2. Each search request deducts 50 credits from your account. Step 2: Monitor Search Progress Utilize the "Check Search Status" endpoint to keep tabs on your search's progress. This action is entirely complimentary. Step 3: Retrieve Results With your search complete, access the results through the "Get Search Result" endpoint. Retrieving each profile incurs a nominal fee of 0.5 credits. For instance, accessing 100 results consumes 50 credits.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-employees'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def big_employee_search(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Having a big employee search? No problem, we now can scrape searches that are up to 50k results. All you need to do is provide the search criteria.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/big-search-employee'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_employees_by_sales_nav_url(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Works exactly the same endpoint "Search Employees" except that it takes a search url as the input. It's helpful when you already have sales navigator search url(s).'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-employees-by-sales-nav-url'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def check_search_status(request_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get the status of your search using the request_id given in step 1.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/check-search-status'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'request_id': request_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_search_results(request_id: Annotated[str, Field(description='')],
                       page: Annotated[str, Field(description='')]) -> dict: 
    '''Get search results. Please make sure the search is "done" before calling this endpoint.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-search-results'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'request_id': request_id,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_companies(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Automate LinkedIn Sales Navigator account searches without connecting your own account. How it works: Step 1: Use this endpoint to make a search using your criteria. This endpoint will return a "request_id" so that you can check for the search status anytime in step 2. This endpoint will cost you 25 credits per request. Step 2: Check the search status using the endpoint "Check Company Search Status" (free). Step 3: Once the search is done, you can start collecting the results by using the endpoint "Get Companies". This endpoint will cost you 0.3 credit per one company. For example, if your search returns 100 results, it'll cost 30 credits.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-companies'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_companies_by_sales_url(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Works exactly the same endpoint "Search Companies" except that it takes a search url as the input. It's helpful when you already have sales navigator search url(s).'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-companies-by-sales-nav-url'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def check_company_search_status(request_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get the status of your search using the request_id given in step 1.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/check-search-companies-status'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'request_id': request_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_companies(request_id: Annotated[str, Field(description='')],
                  page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get search results. Please make sure the search is "done" before calling this endpoint.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-search-companies-results'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'request_id': request_id,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_jobs(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Search jobs posted on LinkedIn. This endpoint is useful for scraping job openings of a specific company on LinkedIn. To scrape all results from each search, change the parameter "start" from 0 to 25, 50, etc. until you see less than 25 results returned. 2 credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-jobs'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_jobs_v2(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Using a simpler payload. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-jobs-v2'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_job_details(job_url: Annotated[str, Field(description='')],
                    include_skills: Annotated[Union[str, None], Field(description='Including skills will cost 1 more credit')] = None,
                    include_hiring_team: Annotated[Union[str, None], Field(description='Including hiring team information will cost 1 more credit')] = None) -> dict: 
    '''Scrape the full job details, including the company basic information. 1 credit per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-job-details'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'job_url': job_url,
        'include_skills': include_skills,
        'include_hiring_team': include_hiring_team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_linkedin_profiles_via_google(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Search LinkedIn profiles via Google by specifying keywords, names, locations, job titles, and companies. This API will retrieve the most relevant profiles from the top 100 Google search results. **2** credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/google-profiles'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_recommendation_given(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get profile’s recommendations (given). **1 credit per call**.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-recommendations-given'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_recommendation_received(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get profile’s recommendations (received). **1 credit per call**.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-recommendations-received'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_years_of_experience(linkedin_url: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get the total number of years of experience of a profile.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-year-of-experiences'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_open_to_work_status(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Given a LinkedIn profile URL, the API will let you know if that profile is “open to work” or not. **1 credit per call.**'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-opentowork-status'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_open_profile_status(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Given a LinkedIn profile URL, the API will let you know if that profile is “open profile” or not. **1 credit per call.**'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-open-profile-status'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_profile_pdf_cv(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get the CV of a LinkedIn profile in PDF format. **1 credit per call.**'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-pdf-cv'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_extra_profile_data(linkedin_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get more profile’s data fields like languages, top skills, certifications, publications, patents, awards'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-extra-profile-data'
    headers = {'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'linkedin_url': linkedin_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_linkedin_company_pages_via_google(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Find up to 100 companies that match your criteria via Google. **2** credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/google-companies'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_companies_instantly(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Search companies in our cached database of 64 million records (updated annually). Instant results. Cost: 1 credit for 10 companies (searches returning fewer than 10 results still consume 1 credit).'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-companies-instantly'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_linkedin_school_pages_via_google(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Find up to 100 schools that match your criteria via Google. **2** credits per call.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/google-schools'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_decision_makers(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Search for decision makers of any company on LinkedIn. This endpoint will remove any unmatched profiles that returned by LinkedIn. It does much more than a simple search on LinkedIn sales navigator. **It takes 50 credits to initiate a search and then takes 0.5 credit per profile returned.** How it works: Step 1: Use this endpoint to make a search using your criteria. This endpoint will return a "request_id" so that you can check for the search status anytime in step 2. This endpoint will cost you 50 credit per request. Step 2: Check the search status using the endpoint "/check-search-status". Calling to this endpoint is FREE. Step 3: Once the search is done, you can start collecting the results by using the endpoint "/get-search-results". This endpoint will cost you 0.5 credit per one profile. For example, if your search returns 100 results, it'll cost 50 credits. **Please note**: it normally takes a few minutes to complete such a search - but sometimes it may need 24 hours. We recommend you put in all your searches and let this api process them all within 24 hours.'''
    url = 'https://fresh-linkedin-profile-data.p.rapidapi.com/search-decision-makers'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'fresh-linkedin-profile-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
