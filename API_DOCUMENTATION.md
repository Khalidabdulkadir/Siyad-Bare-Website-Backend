# React Frontend API Documentation (using Axios)

This guide explains how to interact with the "Legacy of Mohamed Siad Barre" API from a React application using `axios`.

## Base URL

All API endpoints are relative to the base URL. When you run the Django development server, the base URL will be:

```
http://127.0.0.1:8000/
```

## Installing Axios

First, make sure you have `axios` installed in your React project:

```bash
npm install axios
# or
yarn add axios
```

---

## API Endpoints

### 1. Biography

- **Endpoint**: `/api/biography/`
- **Method**: `GET`
- **Description**: Retrieves a list of all biography entries, ordered by year.

**Example Request:**
```javascript
import axios from 'axios';

axios.get('http://127.0.0.1:8000/api/biography/')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('There was an error fetching the biography data!', error);
  });
```

**Example Response (`200 OK`):**
```json
[
    {
        "id": 1,
        "year": 1919,
        "title": "Birth and Early Life",
        "description": "Mohamed Siad Barre was born in the town of Shilavo, Ogaden...",
        "media_url": "http://127.0.0.1:8000/media/biography_media/early_life.jpg"
    }
]
```

### 2. Achievements

- **Endpoint**: `/api/achievements/`
- **Method**: `GET`
- **Description**: Retrieves a list of all achievements.

**Example Request:**
```javascript
axios.get('http://127.0.0.1:8000/api/achievements/')
  .then(response => {
    console.log(response.data);
  });
```

**Example Response (`200 OK`):**
```json
[
    {
        "id": 1,
        "title": "Literacy Campaign",
        "category": "education",
        "description": "A successful nationwide campaign to increase literacy...",
        "image_url": "http://127.0.0.1:8000/media/achievements/literacy_campaign.jpg"
    }
]
```

### 3. Speeches

- **Endpoint**: `/api/speeches/`
- **Method**: `GET`
- **Description**: Retrieves a list of all speeches.

**Example Request:**
```javascript
axios.get('http://127.0.0.1:8000/api/speeches/')
  .then(response => {
    console.log(response.data);
  });
```

**Example Response (`200 OK`):**
```json
[
    {
        "id": 1,
        "title": "The Declaration of Socialism",
        "year": 1969,
        "transcript": "Today we declare that Somalia is a socialist state...",
        "audio_url": "http://127.0.0.1:8000/media/speeches/socialism_declaration.mp3"
    }
]
```

### 4. Gallery

- **Endpoint**: `/api/gallery/`
- **Method**: `GET`
- **Description**: Retrieves a list of all gallery items.

**Example Request:**
```javascript
axios.get('http://127.0.0.1:8000/api/gallery/')
  .then(response => {
    console.log(response.data);
  });
```

**Example Response (`200 OK`):**
```json
[
    {
        "id": 1,
        "title": "Meeting with Foreign Dignitaries",
        "image_url": "http://127.0.0.1:8000/media/gallery/meeting.jpg",
        "category": "Foreign Policy",
        "year": 1974
    }
]
```

### 5. Quiz

- **Endpoint**: `/api/quiz/`
- **Method**: `GET`
- **Description**: Retrieves a list of all quiz questions.

**Example Request:**
```javascript
axios.get('http://127.0.0.1:8000/api/quiz/')
  .then(response => {
    console.log(response.data);
  });
```

**Example Response (`200 OK`):**
```json
[
    {
        "id": 1,
        "question": "In what year did the Somali script standardization occur?",
        "options": ["1960", "1972", "1980", "1991"],
        "correct_answer": "1972"
    }
]
```

### 6. Community Posts

#### A. Get All Posts
- **Endpoint**: `/api/community/`
- **Method**: `GET`
- **Description**: Retrieves a list of all community submissions.

**Example Request:**
```javascript
axios.get('http://127.0.0.1:8000/api/community/')
  .then(response => {
    console.log(response.data);
  });
```

#### B. Create a New Post
- **Endpoint**: `/api/community/`
- **Method**: `POST`
- **Description**: Submits a new post to the community forum. Note the use of `FormData` to handle file uploads.

**Example Request:**
```javascript
import axios from 'axios';

// Assume 'file' is the file object from an <input type="file" />
const file = event.target.files[0]; 

const formData = new FormData();
formData.append('name', 'John Doe');
formData.append('email', 'john.doe@example.com');
formData.append('message', 'This is a great resource!');
if (file) {
  formData.append('photo', file);
}

axios.post('http://127.0.0.1:8000/api/community/', formData, {
  headers: {
    'Content-Type': 'multipart/form-data'
  }
})
.then(response => {
  console.log('Post submitted successfully!', response.data);
})
.catch(error => {
  console.error('There was an error submitting the post!', error);
});
```

**Example Success Response (`201 Created`):**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "This is a great resource!",
    "photo": "http://127.0.0.1:8000/media/community_posts/my_photo.jpg",
    "created_at": "2023-10-21T12:30:00Z"
}
```
